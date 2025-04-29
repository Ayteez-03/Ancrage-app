import streamlit as st
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
    # Si la langue actuelle est le français, passer à l'anglais et vice versa
    if st.session_state.language == "fr":
        st.session_state.language = "en"
    else:
        st.session_state.language = "fr"
    st.rerun()

# Fonction pour mettre à jour la palette de couleurs
def update_color_palette():
    # Obtenir la palette sélectionnée
    selected_palette = st.session_state.selected_palette
    st.session_state.color_palette = selected_palette
    
    # Mettre à jour le fichier de configuration avec la nouvelle palette
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

# Appliquer la palette de couleurs actuelle à la configuration
colors = get_palette_colors(st.session_state.color_palette)

# Configurer la page avec les couleurs actuelles
st.set_page_config(
    page_title="Programme d'Ancrage Psychothérapeutique",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sélecteur de langue et palette de couleurs dans la barre latérale
lang = st.session_state.language
with st.sidebar:
    # Titre et langue
    st.title("🌐")
    if st.button("Change Language"):
        change_language()
    
    # Navigation
    st.markdown("---")
    st.subheader("📍 Navigation")
    
    # Bouton pour retourner à l'accueil
    if st.button("🏠 Retour à l'accueil", key="home_sidebar"):
        st.session_state.current_page = "welcome"
        st.rerun()
    
    # Afficher le bouton de déconnexion si l'utilisateur est authentifié
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        if st.button("🔓 Logout", key="logout_sidebar"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            # Conserver les entrées du journal en mode invité
            st.rerun()
    
    st.markdown("---")
    
    # Paramètres
    st.subheader("Settings")
    
    # Section pour la palette de couleurs
    st.caption("Appearance")
    st.write("Select Color Palette:")
    
    # Obtenir la liste des palettes disponibles
    palettes = get_palette_list(lang)
    palette_options = {p["name"]: p["id"] for p in palettes}
    
    # Sélecteur de palette de couleurs
    current_palette_info = get_palette_display_info(st.session_state.color_palette, lang)
    st.caption("Color Palette Description")
    
    # Utiliser une sélection de radio pour choisir la palette
    selected_palette_name = st.radio(
        label="",
        options=list(palette_options.keys()),
        index=list(palette_options.values()).index(st.session_state.color_palette),
        key="selected_palette_radio"
    )
    
    # Mettre à jour la sélection de palette
    st.session_state.selected_palette = palette_options[selected_palette_name]
    
    # Obtenir les informations sur la palette sélectionnée
    selected_palette_info = get_palette_display_info(st.session_state.selected_palette, lang)
    
    # Afficher une description de la palette sélectionnée
    st.caption(selected_palette_info["description"])
    
    # Afficher un aperçu des couleurs
    preview_cols = st.columns(4)
    with preview_cols[0]:
        st.color_picker("Color 1", selected_palette_info["colors"]["primary"], disabled=True, label_visibility="collapsed")
    with preview_cols[1]:
        st.color_picker("Color 2", selected_palette_info["colors"]["background"], disabled=True, label_visibility="collapsed")
    with preview_cols[2]:
        st.color_picker("Color 3", selected_palette_info["colors"]["secondary_background"], disabled=True, label_visibility="collapsed")
    with preview_cols[3]:
        st.color_picker("Color 4", selected_palette_info["colors"]["text"], disabled=True, label_visibility="collapsed")
    
    # Bouton pour appliquer les changements
    if st.session_state.color_palette != st.session_state.selected_palette:
        st.button("Apply", on_click=update_color_palette)
    
    # Informations sur l'utilisateur connecté (si authentifié)
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        st.markdown("---")
        st.subheader("👤 User")
        st.info(f"Logged in as {st.session_state.username}")
        
    # Ajout du lecteur audio
    add_audio_player_to_sidebar()

# Fonction pour afficher la page d'accueil
def show_welcome():
    st.title("Welcome to the Grounding Program")
    st.markdown("This is a therapeutic grounding tool designed to help you through different techniques.")
    st.button("Start", use_container_width=True, on_click=lambda: setattr(st.session_state, 'current_page', 'questionnaire'))

# Fonction pour afficher le questionnaire
def show_questionnaire():
    if lang == "fr":
        st.title("Questionnaire d'Ancrage")
    else:
        st.title("Grounding Questionnaire")
    
    # Afficher la progression
    progress = st.session_state.question_index / len(questions)
    st.progress(progress)
    
    # Afficher la question actuelle
    question, options = questions[st.session_state.question_index]
    st.subheader(question)
    
    # Afficher les options sous forme de boutons
    for i, option in enumerate(options):
        if st.button(option, key=f"option_{i}", use_container_width=True):
            record_response(i)

# Fonction pour afficher les résultats
def show_results():
    st.title("Your personalized recommendation")
    st.success(f"Your recommended technique is **{st.session_state.technique}**")
    st.markdown(st.session_state.technique_details)

# Importer les pages spéciales
from boite_reussites import show_boite_reussites
from journal_progres import show_journal_page

# Fonction pour changer de page et ouvrir la boîte à réussites
def open_boite_reussites():
    st.session_state.current_page = "boite_reussites"
    st.session_state.boite_reussites_details = True
    st.rerun()

# Fonction pour changer de page et ouvrir le journal de progrès
def open_journal():
    st.session_state.current_page = "journal"
    st.rerun()

# Ajout du bouton de journal sur toutes les pages (sauf le journal lui-même)
if st.session_state.current_page != "journal":
    # Placer le bouton en bas de la sidebar
    with st.sidebar:
        st.markdown("---")
        st.button("Journal", on_click=open_journal, use_container_width=True)

# Affichage des pages en fonction de l'état de session
if st.session_state.current_page == "welcome":
    show_welcome()
elif st.session_state.current_page == "questionnaire":
    show_questionnaire()
elif st.session_state.current_page == "results":
    show_results()
elif st.session_state.current_page == "boite_reussites":
    show_boite_reussites()
elif st.session_state.current_page == "journal":
    show_journal_page()
