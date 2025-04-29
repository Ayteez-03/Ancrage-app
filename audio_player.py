import streamlit as st
from translations import ui_translations

def initialize_audio_state():
    """Initialize audio player state"""
    if 'audio_playing' not in st.session_state:
        st.session_state.audio_playing = False

def toggle_audio():
    """Toggle audio playback state"""
    st.session_state.audio_playing = not st.session_state.audio_playing

def add_audio_player_to_sidebar():
    """Add audio player controls to the sidebar"""
    # Initialize state if not already done
    initialize_audio_state()
    
    # Add a horizontal line for separation
    st.sidebar.markdown("---")
    
    # Get language-specific text
    lang = st.session_state.language
    title = "🎵 " + ("Son d'ambiance" if lang == "fr" else "Ambient Sound")
    description = ("Son apaisant pour faciliter l'ancrage" if lang == "fr" else "Calming sound to aid grounding")
    
    # Add section header
    st.sidebar.subheader(title)
    st.sidebar.markdown(f"##### {description}")
    
    # Create the toggle button with appropriate label based on current state
    if st.session_state.audio_playing:
        button_text = "🔇 " + ("Désactiver le son" if lang == "fr" else "Mute sound")
    else:
        button_text = "🔊 " + ("Activer le son apaisant" if lang == "fr" else "Play calming sound")
    
    # Add the button that toggles audio state
    st.sidebar.button(
        button_text,
        key="audio_toggle_button",
        on_click=toggle_audio,
        type="primary" if st.session_state.audio_playing else "secondary"
    )
    
    # Only show the audio indication when it's playing
    if st.session_state.audio_playing:
        # YouTube iframe embedding with relaxing background music but hidden from view
        youtube_id = "f2YW3YKHcoA"  # "Relaxing Piano Music & Soft Rain Sounds - Relaxing Sleep Music, A Rainy Night"
        
        # Hide the video completely, only playing audio
        embed_html = f"""
        <div style="display:none;">
            <iframe 
                id="youtube_audio" 
                src="https://www.youtube.com/embed/{youtube_id}?autoplay=1&loop=1&playlist={youtube_id}" 
                width="1" 
                height="1" 
                allow="autoplay"
            ></iframe>
        </div>
        <div style="text-align: center; margin-top: 10px;">
            <div style="padding: 8px 12px; background-color: #f0f0f0; border-radius: 4px; display: inline-block;">
                <span style="color: #4CAF50; font-size: 1.2em;">▶</span> 
                <span style="font-size: 0.9em;">
                    {("Musique relaxante de piano avec sons de pluie" if lang == "fr" else "Relaxing piano music with rain sounds")}
                </span>
            </div>
        </div>
        """
        
        # Display sound indicator
        st.sidebar.markdown(embed_html, unsafe_allow_html=True)
        
        # Add status message
        status_text = ("✓ " + ("Son activé" if lang == "fr" else "Sound enabled"))
        st.sidebar.success(status_text)
