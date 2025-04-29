import streamlit as st
import json
from translations import (
    ui_translations, welcome_translations, about_translations,
    success_box_translations, questions_translations, 
    techniques_translations, technique_name_mapping
)
from color_palettes import get_palette_list, get_palette_colors, get_palette_display_info
from audio_player import add_audio_player_to_sidebar

# Initialize session state if not already present
if 'current_page' not in st.session_state:
    st.session_state.current_page = "welcome"
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'responses' not in st.session_state:
    st.session_state.responses = []
if 'technique' not in st.session_state:
    st.session_state.technique = ""
if 'technique_details' not in st.session_state:
    st.session_state.technique_details = ""
if 'boite_reussites_details' not in st.session_state:
    st.session_state.boite_reussites_details = False
if 'language' not in st.session_state:
    st.session_state.language = "fr"  # Langue par défaut: français
if 'color_palette' not in st.session_state:
    st.session_state.color_palette = "default"  # Palette par défaut

# Fonction pour changer de langue
def change_language():
    if st.session_state.language == "fr":
        st.session_state.language = "en"
    else:
        st.session_state.language = "fr"

    if st.session_state.technique:
        technique_fr = st.session_state.technique
        technique_en = technique_name_mapping["en"][technique_fr]

        if st.session_state.language == "en":
            st.session_state.technique = technique_en
            st.session_state.technique_details = techniques_translations["en"][technique_en]
        else:
            st.session_state.technique = technique_fr
            st.session_state.technique_details = techniques_translations["fr"][technique_fr]

    st.rerun()

# Fonction pour mettre à jour la palette de couleurs
def update_color_palette():
    selected_palette = st.session_state.selected_palette
    st.session_state.color_palette = selected_palette

    colors = get_palette_colors(selected_palette)
    with open(".streamlit/config.toml", "w") as f:
        f.write(f"""[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
primaryColor = "{colors['primary']}"
backgroundColor = "{colors['background']}"
secondaryBackgroundColor = "{colors['secondary_background']}"
textColor = "{colors['text']}"
""")

    st.rerun()

colors = get_palette_colors(st.session_state.color_palette)

st.set_page_config(
    page_title="Programme d'Ancrage Psychothérapeutique",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

questions = questions_translations[st.session_state.language]
lang = st.session_state.language  # ✅ ligne ajoutée ici, une fois pour tout le script

with st.sidebar:
    st.title("🌐")
    if st.button(ui_translations[lang]["language_selector"]):
        change_language()

    st.markdown("---")
    st.subheader("📍 " + ("Navigation" if lang == "fr" else "Navigation"))

    if st.button("🏠 " + ("Retour à l'accueil" if lang == "fr" else "Back to home"), key="home_sidebar"):
        st.session_state.current_page = "welcome"
        st.rerun()

    if 'authenticated' in st.session_state and st.session_state.authenticated:
        if st.button("🔓 " + ("Se déconnecter" if lang == "fr" else "Logout"), key="logout_sidebar"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.rerun()

    st.markdown("---")
    st.subheader(ui_translations[lang]["settings_title"])
    st.caption(ui_translations[lang]["appearance_title"])
    st.write(ui_translations[lang]["color_palette_title"])

    palettes = get_palette_list(lang)
    palette_options = {p["name"]: p["id"] for p in palettes}

    current_palette_info = get_palette_display_info(st.session_state.color_palette, lang)
    st.caption(ui_translations[lang]["color_palette_description"])

    selected_palette_name = st.radio(
        label="",
        options=list(palette_options.keys()),
        index=list(palette_options.values()).index(st.session_state.color_palette),
        key="selected_palette_radio"
    )

    st.session_state.selected_palette = palette_options[selected_palette_name]
    selected_palette_info = get_palette_display_info(st.session_state.selected_palette, lang)

    st.caption(selected_palette_info["description"])

    preview_cols = st.columns(4)
    with preview_cols[0]:
        st.color_picker("Color 1", selected_palette_info["colors"]["primary"], disabled=True, label_visibility="collapsed")
    with preview_cols[1]:
        st.color_picker("Color 2", selected_palette_info["colors"]["background"], disabled=True, label_visibility="collapsed")
    with preview_cols[2]:
        st.color_picker("Color 3", selected_palette_info["colors"]["secondary_background"], disabled=True, label_visibility="collapsed")
    with preview_cols[3]:
        st.color_picker("Color 4", selected_palette_info["colors"]["text"], disabled=True, label_visibility="collapsed")

    if st.session_state.color_palette != st.session_state.selected_palette:
        st.button(ui_translations[lang]["apply_button"], on_click=update_color_palette)

    if 'authenticated' in st.session_state and st.session_state.authenticated:
        st.markdown("---")
        st.subheader("👤 " + ("Utilisateur" if lang == "fr" else "User"))
        st.info(ui_translations[lang]["logged_in_as"].format(username=st.session_state.username))

    add_audio_player_to_sidebar()

# [Les autres fonctions restent inchangées, y compris show_questionnaire(), mais on a retiré lang = st.session_state.language de l'intérieur de cette fonction]

# Import des pages spéciales
from boite_reussites import show_boite_reussites
from journal_progres import show_journal_page

def open_boite_reussites():
    st.session_state.current_page = "boite_reussites"
    st.session_state.boite_reussites_details = True
    st.rerun()

def open_journal():
    st.session_state.current_page = "journal"
    st.rerun()

if st.session_state.current_page != "journal":
    with st.sidebar:
        st.markdown("---")
        st.button(
            ui_translations[lang]["journal_button"],
            on_click=open_journal,
            use_container_width=True
        )

# [Affichage des pages inchangé]
if st.session_state.current_page == "welcome":
    show_welcome()
elif st.session_state.current_page == "questionnaire":
    show_questionnaire()
elif st.session_state.current_page == "results":
    show_results()
elif st.session_state.current_page == "about":
    show_about()
elif st.session_state.current_page == "boite_reussites":
    show_boite_reussites()
elif st.session_state.current_page == "journal":
    show_journal_page()
