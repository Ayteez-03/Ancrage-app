import streamlit as st
from translations import ui_translations, success_box_translations

def show_boite_reussites():
    """Affiche les détails sur la technique de la boîte à réussites"""
    lang = st.session_state.language
    translations = success_box_translations[lang]
    
    st.title(translations["title"])
    
    st.markdown(f"""
    ## {translations["how_it_works_title"]}
    
    {translations["how_it_works_text"]}
    
    - {translations["achievements"]}
    - {translations["positive_moments"]}
    - {translations["compliments"]}
    - {translations["mental_images"]}
    
    ## {translations["practice_title"]}
    
    ### {translations["imagination_title"]}
    
    - {translations["imagination_step1"]}
    - {translations["imagination_step2"]}
    - {translations["imagination_step3"]}
    - {translations["imagination_step4"]}
    
    ### {translations["physical_title"]}
    
    - {translations["physical_step1"]}
    - {translations["physical_step2"]}
    - {translations["physical_step3"]}
    """)
    
    st.button(ui_translations[lang]["back_to_results"], use_container_width=True, 
              on_click=lambda: setattr(st.session_state, 'current_page', 'results'))
