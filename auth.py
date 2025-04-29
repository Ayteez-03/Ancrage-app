import streamlit as st
import json
import os
import hashlib
import uuid
from translations import ui_translations

# Dossier pour stocker les données utilisateurs et journaux
DATA_DIR = "user_data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
JOURNALS_DIR = os.path.join(DATA_DIR, "journals")

# Créer les dossiers nécessaires s'ils n'existent pas
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(JOURNALS_DIR, exist_ok=True)

# Initialiser le fichier des utilisateurs s'il n'existe pas
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump({}, f)

def hash_password(password):
    """Hasher un mot de passe pour le stockage sécurisé"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Charger la liste des utilisateurs"""
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    """Sauvegarder la liste des utilisateurs"""
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def register_user(username, password):
    """Enregistrer un nouvel utilisateur"""
    users = load_users()
    
    # Vérifier si l'utilisateur existe déjà
    if username in users:
        return False
    
    # Créer un ID unique pour l'utilisateur
    user_id = str(uuid.uuid4())
    
    # Ajouter l'utilisateur
    users[username] = {
        "password_hash": hash_password(password),
        "user_id": user_id
    }
    
    save_users(users)
    
    # Créer un fichier pour le journal de l'utilisateur
    journal_file = os.path.join(JOURNALS_DIR, f"{user_id}.json")
    if not os.path.exists(journal_file):
        with open(journal_file, "w") as f:
            json.dump([], f)
    
    return True

def authenticate(username, password):
    """Authentifier un utilisateur"""
    users = load_users()
    
    if username not in users:
        return False
    
    if users[username]["password_hash"] != hash_password(password):
        return False
    
    return True

def get_user_id(username):
    """Récupérer l'ID d'un utilisateur"""
    users = load_users()
    
    if username not in users:
        return None
    
    return users[username]["user_id"]

def load_journal(user_id):
    """Charger le journal d'un utilisateur"""
    journal_file = os.path.join(JOURNALS_DIR, f"{user_id}.json")
    
    if not os.path.exists(journal_file):
        return []
    
    with open(journal_file, "r") as f:
        return json.load(f)

def save_journal(user_id, journal_entries):
    """Sauvegarder le journal d'un utilisateur"""
    journal_file = os.path.join(JOURNALS_DIR, f"{user_id}.json")
    
    # Convertir les dates en chaînes pour le stockage JSON
    serializable_entries = []
    for entry in journal_entries:
        serializable_entry = entry.copy()
        if isinstance(entry["date"], (str, int, float, bool, type(None))):
            # Déjà sérialisable
            pass
        else:
            # Convertir la date en chaîne
            serializable_entry["date"] = entry["date"].strftime("%Y-%m-%d")
        serializable_entries.append(serializable_entry)
    
    with open(journal_file, "w") as f:
        json.dump(serializable_entries, f)

def show_login_form():
    """Afficher le formulaire de connexion/inscription"""
    lang = st.session_state.language
    translations = ui_translations[lang]
    
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'register_mode' not in st.session_state:
        st.session_state.register_mode = False
    
    # Si l'utilisateur est déjà authentifié, afficher un message
    if st.session_state.authenticated:
        logged_in_text = translations["logged_in_as"].format(username=st.session_state.username)
        st.success(f"✅ {logged_in_text}")
        
        # Bouton de déconnexion
        if st.button(translations["logout_button"]):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.rerun()
        
        return
    
    # Titre du formulaire
    st.subheader(translations["login_title"])
    
    # Description de la connexion
    st.caption(translations["login_desc"])
    
    # Onglets pour basculer entre connexion et inscription
    tab1, tab2 = st.tabs([translations["login_tab"], translations["register_tab"]])
    
    with tab1:
        with st.form("login_form"):
            username = st.text_input(translations["username"])
            password = st.text_input(translations["password"], type="password")
            submit_login = st.form_submit_button(translations["login_button"])
            
            if submit_login:
                if username and password:
                    if authenticate(username, password):
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        
                        # Charger le journal de l'utilisateur
                        user_id = get_user_id(username)
                        st.session_state.user_id = user_id
                        st.session_state.journal_entries = load_journal(user_id)
                        
                        st.success(f"✅ {translations['login_success']}")
                        st.rerun()
                    else:
                        st.error(translations["login_error"])
                else:
                    st.warning(translations["fields_required"])
    
    with tab2:
        with st.form("register_form"):
            new_username = st.text_input(translations["username"])
            new_password = st.text_input(translations["password"], type="password")
            confirm_password = st.text_input(translations["confirm_password"], type="password")
            submit_register = st.form_submit_button(translations["register_button"])
            
            if submit_register:
                if new_username and new_password and confirm_password:
                    if new_password != confirm_password:
                        st.error(translations["password_mismatch"])
                    else:
                        if register_user(new_username, new_password):
                            st.success(f"✅ {translations['register_success']}")
                            # Passer automatiquement en mode connexion
                            st.rerun()
                        else:
                            st.error(translations["register_error"])
                else:
                    st.warning(translations["fields_required"])
