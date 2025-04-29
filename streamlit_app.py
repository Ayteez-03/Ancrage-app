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
    # Si la langue actuelle est le français, passer à l'anglais et vice versa
    if st.session_state.language == "fr":
        st.session_state.language = "en"
    else:
        st.session_state.language = "fr"
    
    # Si l'utilisateur a déjà obtenu un résultat, mettre à jour le texte des résultats
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
    if st.button(ui_translations[lang]["language_selector"]):
        change_language()
    
    # Navigation
    st.markdown("---")
    st.subheader("📍 " + ("Navigation" if lang == "fr" else "Navigation"))
    
    # Bouton pour retourner à l'accueil
    if st.button("🏠 " + ("Retour à l'accueil" if lang == "fr" else "Back to home"), key="home_sidebar"):
        st.session_state.current_page = "welcome"
        st.rerun()
    
    # Afficher le bouton de déconnexion si l'utilisateur est authentifié
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        if st.button("🔓 " + ("Se déconnecter" if lang == "fr" else "Logout"), key="logout_sidebar"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            # Conserver les entrées du journal en mode invité
            st.rerun()
    
    st.markdown("---")
    
    # Paramètres
    st.subheader(ui_translations[lang]["settings_title"])
    
    # Section pour la palette de couleurs
    st.caption(ui_translations[lang]["appearance_title"])
    st.write(ui_translations[lang]["color_palette_title"])
    
    # Obtenir la liste des palettes disponibles
    palettes = get_palette_list(lang)
    palette_options = {p["name"]: p["id"] for p in palettes}
    
    # Sélecteur de palette de couleurs
    current_palette_info = get_palette_display_info(st.session_state.color_palette, lang)
    st.caption(ui_translations[lang]["color_palette_description"])
    
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
        st.button(ui_translations[lang]["apply_button"], on_click=update_color_palette)
    
    # Informations sur l'utilisateur connecté (si authentifié)
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        st.markdown("---")
        st.subheader("👤 " + ("Utilisateur" if lang == "fr" else "User"))
        st.info(ui_translations[lang]["logged_in_as"].format(username=st.session_state.username))
        
    # Ajout du lecteur audio
    add_audio_player_to_sidebar()

# Obtenir les questions en fonction de la langue sélectionnée
questions = questions_translations[st.session_state.language]

def analyser_reponses(reponses):
    """Analyse les réponses et détermine la technique d'ancrage"""
    corps_score = 0
    orientation_score = 0
    imagination_score = 0

    for i, reponse in enumerate(reponses):
        if i == 0:  # Question 1 (Yeux fermés)
            if reponse == 1: orientation_score += 1
            elif reponse == 2: corps_score += 1
        elif i == 1:  # Question 2 (Sensations corporelles)
            if reponse == 0: corps_score += 2
            elif reponse == 1: imagination_score += 1
        elif i == 2:  # Question 3 (Réaction émotionnelle)
            if reponse == 0: corps_score += 1
            elif reponse == 1: orientation_score += 1
            elif reponse == 2: imagination_score += 1
        elif i == 3:  # Question 4 (Exercice physique)
            if reponse == 0: corps_score += 1
        elif i == 4:  # Question 5 (Souvenirs ou imagination)
            if reponse == 0: imagination_score += 1
            elif reponse == 1: corps_score += 1
        elif i == 5:  # Question 6 (Distractions)
            if reponse == 0: imagination_score += 1
            elif reponse == 1: orientation_score += 1
            elif reponse == 2: corps_score += 1
        elif i == 6:  # Question 7 (Éléments environnementaux)
            if reponse == 0: orientation_score += 1
            elif reponse == 1: imagination_score += 1
            elif reponse == 2: corps_score += 1

    # Déterminer la technique d'ancrage
    technique_fr = None
    if corps_score > orientation_score and corps_score > imagination_score:
        technique_fr = "Techniques d'ancrage centrées sur le corps"
    elif orientation_score > corps_score and orientation_score > imagination_score:
        technique_fr = "Techniques d'ancrage centrées sur l'orientation"
    elif imagination_score > corps_score and imagination_score > orientation_score:
        technique_fr = "Techniques d'ancrage centrées sur l'imagination"
    else:
        technique_fr = "Mélange de techniques"
        
    # Retourner la technique dans la langue sélectionnée
    if st.session_state.language == "en":
        return technique_name_mapping["en"][technique_fr]
    else:
        return technique_fr

def reset_questionnaire():
    """Réinitialise le questionnaire"""
    st.session_state.current_page = "welcome"
    st.session_state.question_index = 0
    st.session_state.responses = []
    st.session_state.technique = ""
    st.session_state.technique_details = ""
    st.rerun()

def record_response(response):
    """Enregistre la réponse et passe à la question suivante"""
    st.session_state.responses.append(response)
    st.session_state.question_index += 1
    
    # Si toutes les questions ont été posées, afficher la recommandation
    if st.session_state.question_index >= len(questions):
        technique = analyser_reponses(st.session_state.responses)
        st.session_state.technique = technique
        
        # Récupérer les détails de la technique dans la langue sélectionnée
        if st.session_state.language == "en":
            st.session_state.technique_details = techniques_translations["en"][technique]
        else:
            st.session_state.technique_details = techniques_translations["fr"][technique]
            
        st.session_state.current_page = "results"
    st.rerun()

def show_welcome():
    """Affiche la page d'accueil"""
    lang = st.session_state.language
    translations = welcome_translations[lang]
    
    st.title(translations["title"])
    
    st.markdown(f"""
    {translations["welcome_text"]}
    
    ## {translations["what_is_title"]}
    
    {translations["what_is_text"]}
    
    ## {translations["about_questionnaire_title"]}
    
    {translations["about_questionnaire_text"]}
    
    {translations["ready_text"]}
    """)
    
    st.button(ui_translations[lang]["start_button"], use_container_width=True, 
              on_click=lambda: setattr(st.session_state, 'current_page', 'questionnaire'))

def show_about():
    """Affiche la page À propos"""
    lang = st.session_state.language
    translations = about_translations[lang]
    
    st.title(translations["title"])
    
    st.markdown(f"""
    ## {translations["methodology_title"]}
    
    {translations["methodology_text"]}
    
    {translations["questionnaire_eval"]}
    
    1. {translations["body_techniques"]}
    2. {translations["orientation_techniques"]}
    3. {translations["imagination_techniques"]}
    
    ## {translations["effectiveness_title"]}
    
    {translations["effectiveness_text"]}
    
    {translations["useful_for"]}
    - {translations["useful_anxiety"]}
    - {translations["useful_ptsd"]}
    - {translations["useful_dissociation"]}
    - {translations["useful_panic"]}
    - {translations["useful_emotions"]}
    
    ## {translations["regular_practice_title"]}
    
    {translations["regular_practice_text"]}
    """)
    
    st.button(ui_translations[lang]["back_to_results"], use_container_width=True, 
              on_click=lambda: setattr(st.session_state, 'current_page', 'results'))
    st.button(ui_translations[lang]["restart_button"], use_container_width=True, 
              on_click=reset_questionnaire)

def show_questionnaire():
    """Affiche le questionnaire"""
    lang = st.session_state.language
    
    if lang == "fr":
        st.title("Questionnaire d'Ancrage")
    else:
        st.title("Grounding Questionnaire")
    
    # Afficher la progression
    progress = st.session_state.question_index / len(questions)
    st.progress(progress)
    
    progress_text = ui_translations[lang]["question_progress"].format(
        current=st.session_state.question_index + 1, 
        total=len(questions)
    )
    st.write(progress_text)
    
    # Afficher la question actuelle
    question, options = questions[st.session_state.question_index]
    st.subheader(question)
    
    # Afficher les options sous forme de boutons
    for i, option in enumerate(options):
        if st.button(option, key=f"option_{i}", use_container_width=True):
            record_response(i)

def show_results():
    """Affiche les résultats et recommandations"""
    lang = st.session_state.language
    
    if lang == "fr":
        st.title("Votre recommandation personnalisée")
    else:
        st.title("Your personalized recommendation")
    
    st.success(f"{ui_translations[lang]['recommendation_intro']} **{st.session_state.technique}**")
    
    st.markdown(st.session_state.technique_details)
    
    # Bouton pour la boîte à réussites seulement pour les techniques d'imagination
    if (lang == "fr" and st.session_state.technique == "Techniques d'ancrage centrées sur l'imagination") or \
       (lang == "en" and st.session_state.technique == "Imagination-centered grounding techniques"):
        st.button(ui_translations[lang]["success_box_button"], use_container_width=True, 
                  on_click=open_boite_reussites, key="boite_main_btn")
        st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button(ui_translations[lang]["more_info_button"], use_container_width=True, 
                  on_click=lambda: setattr(st.session_state, 'current_page', 'about'))
    with col2:
        st.button(ui_translations[lang]["restart_button"], use_container_width=True, 
                  on_click=reset_questionnaire)

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
        st.button(
            ui_translations[lang]["journal_button"],
            on_click=open_journal,
            use_container_width=True
        )

# Affichage des pages en fonction de l'état de session
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
