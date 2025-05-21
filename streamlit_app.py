import streamlit as st
from translations import (
    ui_translations, welcome_translations, about_translations,
    success_box_translations, questions_translations, 
    techniques_translations, technique_name_mapping
)
from color_palettes import get_palette_list, get_palette_colors, get_palette_display_info
from audio_player import add_audio_player_to_sidebar
from boite_reussites import show_boite_reussites
from journal_progres import show_journal_page

# ---- INIT SESSION STATE ----
for key, default in [
    ('current_page', "welcome"),
    ('question_index', 0),
    ('responses', []),
    ('technique', ""),
    ('technique_details', ""),
    ('boite_reussites_details', False),
    ('language', "fr"),  # Default language: French
    ('color_palette', "default"),
]:
    if key not in st.session_state:
        st.session_state[key] = default

# ---- CALLBACKS ----
def change_language():
    lang = st.session_state.language
    other_lang = "en" if lang == "fr" else "fr"
    st.session_state.language = other_lang
    # Update result text if result is shown
    if st.session_state.technique:
        tech_fr = st.session_state.technique
        tech_en = technique_name_mapping["en"].get(tech_fr, tech_fr)
        if other_lang == "en":
            st.session_state.technique = tech_en
            st.session_state.technique_details = techniques_translations["en"].get(tech_en, "")
        else:
            st.session_state.technique = tech_fr
            st.session_state.technique_details = techniques_translations["fr"].get(tech_fr, "")
    st.experimental_rerun()

def update_color_palette():
    selected = st.session_state.selected_palette
    st.session_state.color_palette = selected
    st.experimental_rerun()

def reset_questionnaire():
    st.session_state.current_page = "welcome"
    st.session_state.question_index = 0
    st.session_state.responses = []
    st.session_state.technique = ""
    st.session_state.technique_details = ""
    st.experimental_rerun()

def record_response(response):
    st.session_state.responses.append(response)
    st.session_state.question_index += 1
    questions = questions_translations[st.session_state.language]
    if st.session_state.question_index >= len(questions):
        technique = analyser_reponses(st.session_state.responses)
        st.session_state.technique = technique
        st.session_state.technique_details = techniques_translations[st.session_state.language].get(technique, "")
        st.session_state.current_page = "results"
    st.experimental_rerun()

def open_boite_reussites():
    st.session_state.current_page = "boite_reussites"
    st.session_state.boite_reussites_details = True
    st.experimental_rerun()

def open_journal():
    st.session_state.current_page = "journal"
    st.experimental_rerun()

# ---- PAGE CONFIG ----
colors = get_palette_colors(st.session_state.color_palette)
st.set_page_config(
    page_title="Programme d'Ancrage Psychothérapeutique",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- SIDEBAR ----
lang = st.session_state.language
with st.sidebar:
    st.title("🌐")
    st.button(ui_translations[lang]["language_selector"], on_click=change_language)
    st.markdown("---")
    st.subheader("📍 Navigation")
    st.button("🏠 " + ("Retour à l'accueil" if lang == "fr" else "Back to home"),
              key="home_sidebar", on_click=lambda: st.session_state.update({"current_page": "welcome"}))
    if st.session_state.get('authenticated'):
        st.button("🔓 " + ("Se déconnecter" if lang == "fr" else "Logout"),
                  key="logout_sidebar",
                  on_click=lambda: st.session_state.update({"authenticated": False, "username": ""}))
    st.markdown("---")
    st.subheader(ui_translations[lang]["settings_title"])
    st.caption(ui_translations[lang]["appearance_title"])
    st.write(ui_translations[lang]["color_palette_title"])
    palettes = get_palette_list(lang)
    palette_options = {p["name"]: p["id"] for p in palettes}
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
    color_keys = ["primary", "background", "secondary_background", "text"]
    for i, col in enumerate(preview_cols):
        with col:
            st.color_picker(f"Color {i+1}", selected_palette_info["colors"][color_keys[i]], disabled=True, label_visibility="collapsed")
    if st.session_state.color_palette != st.session_state.selected_palette:
        st.button(ui_translations[lang]["apply_button"], on_click=update_color_palette)
    if st.session_state.get('authenticated'):
        st.markdown("---")
        st.subheader("👤 " + ("Utilisateur" if lang == "fr" else "User"))
        st.info(ui_translations[lang]["logged_in_as"].format(username=st.session_state.username))
    add_audio_player_to_sidebar()
    if st.session_state.current_page != "journal":
        st.markdown("---")
        st.button(
            ui_translations[lang]["journal_button"],
            on_click=open_journal,
            use_container_width=True,
        )

# ---- LOGIC: QUESTIONS & ANALYSIS ----
def analyser_reponses(reponses):
    corps_score = orientation_score = imagination_score = 0
    for i, reponse in enumerate(reponses):
        if i == 0:
            if reponse == 1: orientation_score += 1
            elif reponse == 2: corps_score += 1
        elif i == 1:
            if reponse == 0: corps_score += 2
            elif reponse == 1: imagination_score += 1
        elif i == 2:
            if reponse == 0: corps_score += 1
            elif reponse == 1: orientation_score += 1
            elif reponse == 2: imagination_score += 1
        elif i == 3:
            if reponse == 0: corps_score += 1
        elif i == 4:
            if reponse == 0: imagination_score += 1
            elif reponse == 1: corps_score += 1
        elif i == 5:
            if reponse == 0: imagination_score += 1
            elif reponse == 1: orientation_score += 1
            elif reponse == 2: corps_score += 1
        elif i == 6:
            if reponse == 0: orientation_score += 1
            elif reponse == 1: imagination_score += 1
            elif reponse == 2: corps_score += 1
    if corps_score > orientation_score and corps_score > imagination_score:
        tech_fr = "Techniques d'ancrage centrées sur le corps"
    elif orientation_score > corps_score and orientation_score > imagination_score:
        tech_fr = "Techniques d'ancrage centrées sur l'orientation"
    elif imagination_score > corps_score and imagination_score > orientation_score:
        tech_fr = "Techniques d'ancrage centrées sur l'imagination"
    else:
        tech_fr = "Mélange de techniques"
    return technique_name_mapping["en"][tech_fr] if st.session_state.language == "en" else tech_fr

# ---- PAGES ----
def show_welcome():
    t = welcome_translations[lang]
    st.title(t["title"])
    st.markdown(f"""
    {t["welcome_text"]}
    ## {t["what_is_title"]}
    {t["what_is_text"]}
    ## {t["about_questionnaire_title"]}
    {t["about_questionnaire_text"]}
    {t["ready_text"]}
    """)
    st.button(ui_translations[lang]["start_button"], use_container_width=True,
              on_click=lambda: st.session_state.update({"current_page": "questionnaire"}))

def show_about():
    t = about_translations[lang]
    st.title(t["title"])
    st.markdown(f"""
    ## {t["methodology_title"]}
    {t["methodology_text"]}
    {t["questionnaire_eval"]}
    1. {t["body_techniques"]}
    2. {t["orientation_techniques"]}
    3. {t["imagination_techniques"]}
    ## {t["effectiveness_title"]}
    {t["effectiveness_text"]}
    {t["useful_for"]}
    - {t["useful_anxiety"]}
    - {t["useful_ptsd"]}
    - {t["useful_dissociation"]}
    - {t["useful_panic"]}
    - {t["useful_emotions"]}
    ## {t["regular_practice_title"]}
    {t["regular_practice_text"]}
    """)
    st.button(ui_translations[lang]["back_to_results"], use_container_width=True,
              on_click=lambda: st.session_state.update({"current_page": "results"}))
    st.button(ui_translations[lang]["restart_button"], use_container_width=True,
              on_click=reset_questionnaire)

def show_questionnaire():
    questions = questions_translations[st.session_state.language]
    st.title("Questionnaire d'Ancrage" if lang == "fr" else "Grounding Questionnaire")
    progress = st.session_state.question_index / len(questions)
    st.progress(progress)
    st.write(ui_translations[lang]["question_progress"].format(
        current=st.session_state.question_index + 1, total=len(questions)))
    question, options = questions[st.session_state.question_index]
    st.subheader(question)
    for i, option in enumerate(options):
        st.button(option, key=f"option_{i}", use_container_width=True, on_click=lambda i=i: record_response(i))

def show_results():
    st.title("Votre recommandation personnalisée" if lang == "fr" else "Your personalized recommendation")
    st.success(f"{ui_translations[lang]['recommendation_intro']} **{st.session_state.technique}**")
    st.markdown(st.session_state.technique_details)
    if (lang == "fr" and st.session_state.technique == "Techniques d'ancrage centrées sur l'imagination") or \
       (lang == "en" and st.session_state.technique == "Imagination-centered grounding techniques"):
        st.button(ui_translations[lang]["success_box_button"], use_container_width=True, on_click=open_boite_reussites)
        st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.button(ui_translations[lang]["more_info_button"], use_container_width=True,
                  on_click=lambda: st.session_state.update({"current_page": "about"}))
    with col2:
        st.button(ui_translations[lang]["restart_button"], use_container_width=True, on_click=reset_questionnaire)

# ---- PAGE ROUTER ----
page = st.session_state.current_page
if page == "welcome":
    show_welcome()
elif page == "questionnaire":
    show_questionnaire()
elif page == "results":
    show_results()
elif page == "about":
    show_about()
elif page == "boite_reussites":
    show_boite_reussites()
elif page == "journal":
    show_journal_page()
