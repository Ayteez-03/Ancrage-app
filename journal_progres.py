import streamlit as st
import pandas as pd
import datetime
import altair as alt
from translations import ui_translations
from auth import show_login_form, save_journal, load_journal

def initialize_journal_data():
    """Initialise les données du journal si elles n'existent pas déjà"""
    if 'journal_entries' not in st.session_state:
        st.session_state.journal_entries = []
    
    # Si l'utilisateur est authentifié mais que son journal n'est pas chargé
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        if 'user_id' in st.session_state and 'journal_entries' not in st.session_state:
            st.session_state.journal_entries = load_journal(st.session_state.user_id)

def add_journal_entry(date, context, sud_before, sud_after, technique, notes):
    """Ajoute une entrée au journal de progrès et sauvegarde si l'utilisateur est authentifié"""
    entry = {
        "date": date,
        "context": context,
        "sud_before": sud_before,
        "sud_after": sud_after,
        "technique": technique,
        "notes": notes
    }
    st.session_state.journal_entries.append(entry)
    
    # Sauvegarder le journal si l'utilisateur est authentifié
    if 'authenticated' in st.session_state and st.session_state.authenticated:
        if 'user_id' in st.session_state:
            save_journal(st.session_state.user_id, st.session_state.journal_entries)

def get_consecutive_days():
    """Calcule le nombre de jours consécutifs d'ancrage"""
    if not st.session_state.journal_entries:
        return 0
        
    # Convertir les dates au format datetime si nécessaire
    entries_with_datetime = []
    for entry in st.session_state.journal_entries:
        entry_copy = entry.copy()
        # Si la date est une chaîne, la convertir en objet datetime
        if isinstance(entry["date"], str):
            try:
                entry_copy["date"] = datetime.datetime.strptime(entry["date"], "%Y-%m-%d").date()
            except ValueError:
                # Si le format ne correspond pas, utiliser la date d'aujourd'hui
                entry_copy["date"] = datetime.date.today()
        entries_with_datetime.append(entry_copy)
        
    # Trier les entrées par date
    sorted_entries = sorted(entries_with_datetime, key=lambda x: x["date"])
    
    # Calculer les jours consécutifs
    if len(sorted_entries) <= 1:
        return len(sorted_entries)
        
    consecutive_days = 1
    max_consecutive = 1
    
    for i in range(1, len(sorted_entries)):
        current_date = sorted_entries[i]["date"]
        prev_date = sorted_entries[i-1]["date"]
        
        # Vérifier si les dates sont consécutives
        if isinstance(current_date, datetime.date) and isinstance(prev_date, datetime.date):
            if (current_date - prev_date).days == 1:
                consecutive_days += 1
                max_consecutive = max(max_consecutive, consecutive_days)
            elif (current_date - prev_date).days > 1:
                consecutive_days = 1
            
    return max_consecutive

def get_average_sud_difference():
    """Calcule la différence moyenne entre les SUD avant et après"""
    if not st.session_state.journal_entries:
        return 0
    
    # S'assurer que les valeurs SUD sont des nombres
    total_diff = 0
    for entry in st.session_state.journal_entries:
        sud_before = entry["sud_before"]
        sud_after = entry["sud_after"]
        
        # Convertir en nombres si ce sont des chaînes
        if isinstance(sud_before, str):
            try:
                sud_before = float(sud_before)
            except (ValueError, TypeError):
                sud_before = 0
                
        if isinstance(sud_after, str):
            try:
                sud_after = float(sud_after)
            except (ValueError, TypeError):
                sud_after = 0
        
        # Calculer la différence
        total_diff += (sud_before - sud_after)
    
    return total_diff / len(st.session_state.journal_entries)

def show_journal_page():
    """Affiche la page du journal de progrès"""
    initialize_journal_data()
    
    lang = st.session_state.language
    translations = ui_translations[lang]
    
    title = "Journal de Progrès d'Ancrage" if lang == "fr" else "Grounding Progress Journal"
    st.title(f"📖 {title}")
    
    # Vérifier si l'utilisateur est authentifié
    authenticated = 'authenticated' in st.session_state and st.session_state.authenticated
    
    # Si l'utilisateur n'est pas authentifié, afficher le formulaire de connexion
    if not authenticated:
        st.warning(f"⚠️ {translations['login_required']}")
        show_login_form()
        
        # Afficher un séparateur
        st.markdown("---")
        st.markdown(f"### {translations['guest_mode']}")
        st.caption(f"⚠️ {translations['guest_warning']}")
    else:
        # Afficher un message de bienvenue personnalisé
        logged_in_text = translations["logged_in_as"].format(username=st.session_state.username)
        st.success(f"✅ {logged_in_text} {translations['autosave']}")
    
    # Statistiques
    st.subheader("📊 " + ("Statistiques" if lang == "fr" else "Statistics"))
    
    consecutive_days = get_consecutive_days()
    consecutive_text = f"{consecutive_days} " + ("jours consécutifs" if lang == "fr" else "consecutive days")
    st.metric(
        label=("Engagement" if lang == "fr" else "Engagement"), 
        value=consecutive_text
    )
    
    st.markdown("---")
    
    # Formulaire pour ajouter une entrée
    st.subheader("➕ " + ("Ajouter une entrée" if lang == "fr" else "Add an entry"))
    
    with st.form("journal_entry_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            date = st.date_input(
                ("Date" if lang == "fr" else "Date"),
                value=datetime.date.today()
            )
            
            sud_before = st.slider(
                ("SUD* avant (0-10)" if lang == "fr" else "SUD* before (0-10)"),
                min_value=0,
                max_value=10,
                value=5,
                help=("*SUD = Niveau de perturbation subjectif" if lang == "fr" else "*SUD = Subjective units of distress")
            )
            
            technique = st.selectbox(
                ("Technique utilisée" if lang == "fr" else "Technique used"),
                options=[
                    ("Techniques d'ancrage centrées sur le corps" if lang == "fr" else "Body-centered grounding techniques"),
                    ("Techniques d'ancrage centrées sur l'orientation" if lang == "fr" else "Orientation-centered grounding techniques"),
                    ("Techniques d'ancrage centrées sur l'imagination" if lang == "fr" else "Imagination-centered grounding techniques"),
                    ("Mélange de techniques" if lang == "fr" else "Mix of techniques")
                ]
            )
        
        with col2:
            context = st.text_input(
                ("Contexte ou situation" if lang == "fr" else "Context or situation")
            )
            
            sud_after = st.slider(
                ("SUD* après (0-10)" if lang == "fr" else "SUD* after (0-10)"),
                min_value=0,
                max_value=10,
                value=3,
                help=("*SUD = Niveau de perturbation subjectif" if lang == "fr" else "*SUD = Subjective units of distress")
            )
            
            notes = st.text_area(
                ("Notes ou observations" if lang == "fr" else "Notes or observations"),
                height=100
            )
        
        submit_text = "Ajouter au journal" if lang == "fr" else "Add to journal"
        submit = st.form_submit_button(submit_text, use_container_width=True)
        
        if submit:
            add_journal_entry(date, context, sud_before, sud_after, technique, notes)
            st.success("✅ " + ("Entrée ajoutée avec succès" if lang == "fr" else "Entry added successfully"))
            st.rerun()
    
    st.markdown("---")
    
    # Afficher le journal
    st.subheader("📝 " + ("Mes entrées de journal" if lang == "fr" else "My journal entries"))
    
    if not st.session_state.journal_entries:
        st.info("📝 " + 
            ("Votre journal est vide. Ajoutez votre première entrée ci-dessus!" if lang == "fr" 
             else "Your journal is empty. Add your first entry above!")
        )
    else:
        # Convertir les entrées en dataframe pour l'affichage
        entries_df = pd.DataFrame(st.session_state.journal_entries)
        
        # Créer des noms de colonnes lisibles
        if lang == "fr":
            entries_df.columns = ["Date", "Contexte", "SUD avant", "SUD après", "Technique", "Notes"]
        else:
            entries_df.columns = ["Date", "Context", "SUD before", "SUD after", "Technique", "Notes"]
        
        st.dataframe(entries_df, use_container_width=True)
        
        # Visualisation graphique
        st.subheader("📈 " + ("Visualisation" if lang == "fr" else "Visualization"))
        
        # Préparer les données pour la visualisation
        chart_data = []
        for entry in st.session_state.journal_entries:
            # Convertir les dates au format datetime si nécessaire
            entry_date = entry["date"]
            if isinstance(entry_date, str):
                try:
                    entry_date = datetime.datetime.strptime(entry_date, "%Y-%m-%d").date()
                except ValueError:
                    # Si le format ne correspond pas, utiliser la date d'aujourd'hui
                    entry_date = datetime.date.today()
            
            # Convertir les SUD en nombres si nécessaire
            sud_before = entry["sud_before"]
            if isinstance(sud_before, str):
                try:
                    sud_before = float(sud_before)
                except (ValueError, TypeError):
                    sud_before = 0
                    
            sud_after = entry["sud_after"]
            if isinstance(sud_after, str):
                try:
                    sud_after = float(sud_after)
                except (ValueError, TypeError):
                    sud_after = 0
                    
            # Ajouter les données au graphique
            chart_data.append({
                "date": entry_date,
                "SUD": sud_before,
                "type": "avant" if lang == "fr" else "before"
            })
            chart_data.append({
                "date": entry_date,
                "SUD": sud_after,
                "type": "après" if lang == "fr" else "after"
            })
        
        if chart_data:  # Vérifier que nous avons des données
            chart_df = pd.DataFrame(chart_data)
            
            # Trier par date
            chart_df = chart_df.sort_values(by="date")
            
            try:
                # Créer le graphique
                chart = alt.Chart(chart_df).mark_line(point=True).encode(
                    x='date:T',
                    y=alt.Y('SUD:Q', scale=alt.Scale(domain=[0, 10])),
                    color='type:N',
                    tooltip=['date:T', 'SUD:Q', 'type:N']
                ).properties(
                    width="container",
                    height=300,
                    title=("Évolution des niveaux de perturbation (SUD)" if lang == "fr" 
                          else "Evolution of distress levels (SUD)")
                )
                
                st.altair_chart(chart, use_container_width=True)
            except Exception as e:
                st.error(f"Erreur lors de la création du graphique: {e}")
        else:
            st.info("Pas assez de données pour afficher un graphique" if lang == "fr" else "Not enough data to display a chart")
        
        # Explication du SUD
        st.caption("*SUD = " + 
            ("Niveau de perturbation subjectif, entre 0 et 10. 0 étant \"pas du tout perturbé\" et 10 \"extrêmement perturbé\"" 
             if lang == "fr" else 
             "Subjective units of distress, between 0 and 10. 0 being \"not disturbed at all\" and 10 \"extremely disturbed\"")
        )
    
    # Bouton de retour
    st.button(
        ("Retour à l'accueil" if lang == "fr" else "Back to home"), 
        key="return_from_journal",
        on_click=lambda: setattr(st.session_state, 'current_page', 'welcome'),
        use_container_width=True
    )
