"""
Module contenant les palettes de couleurs apaisantes pour l'application.
"""

# Palettes de couleurs apaisantes
calming_palettes = {
    "default": {
        "name": {
            "fr": "Défaut",
            "en": "Default"
        },
        "colors": {
            "primary": "#5e55d9",
            "background": "#f5f7f9",
            "secondary_background": "#e6eaf1",
            "text": "#262730"
        },
        "description": {
            "fr": "La palette par défaut avec des tons lavande apaisants.",
            "en": "The default palette with soothing lavender tones."
        }
    },
    "ocean": {
        "name": {
            "fr": "Océan",
            "en": "Ocean"
        },
        "colors": {
            "primary": "#4a8db7",
            "background": "#f0f5f9",
            "secondary_background": "#dbe9f4",
            "text": "#2c3e50"
        },
        "description": {
            "fr": "Des bleus profonds inspirés par l'océan pour un effet calmant.",
            "en": "Deep blues inspired by the ocean for a calming effect."
        }
    },
    "forest": {
        "name": {
            "fr": "Forêt",
            "en": "Forest"
        },
        "colors": {
            "primary": "#3e8957",
            "background": "#f2f7f2",
            "secondary_background": "#e3efe4",
            "text": "#2d3c2d"
        },
        "description": {
            "fr": "Des tons verts apaisant comme une promenade en forêt.",
            "en": "Soothing green tones like a walk in the forest."
        }
    },
    "sunset": {
        "name": {
            "fr": "Coucher de soleil",
            "en": "Sunset"
        },
        "colors": {
            "primary": "#d98555",
            "background": "#fdf7f2",
            "secondary_background": "#f9e8dd",
            "text": "#532f1c"
        },
        "description": {
            "fr": "Des teintes chaudes et douces de coucher de soleil.",
            "en": "Warm and soft sunset hues."
        }
    },
    "lavender": {
        "name": {
            "fr": "Lavande",
            "en": "Lavender"
        },
        "colors": {
            "primary": "#9b7ed9",
            "background": "#f7f5fd",
            "secondary_background": "#ebe6f9",
            "text": "#3a2c58"
        },
        "description": {
            "fr": "Des tons violets doux comme les champs de lavande.",
            "en": "Soft purple tones like lavender fields."
        }
    },
    "moonlight": {
        "name": {
            "fr": "Clair de lune",
            "en": "Moonlight"
        },
        "colors": {
            "primary": "#6f8da9",
            "background": "#f5f8fc",
            "secondary_background": "#e9eff5",
            "text": "#323c46"
        },
        "description": {
            "fr": "Des tons bleu-gris doux inspirés par la lumière de la lune.",
            "en": "Soft blue-gray tones inspired by moonlight."
        }
    }
}

# Traduire les noms et descriptions des palettes
def get_palette_display_info(palette_id, language):
    """
    Récupère les informations d'affichage d'une palette dans la langue spécifiée.

    Args:
        palette_id (str): Identifiant de la palette
        language (str): Code de langue ('fr' ou 'en')

    Returns:
        dict: Nom et description de la palette dans la langue spécifiée
    """
    palette = calming_palettes.get(palette_id, calming_palettes["default"])
    return {
        "name": palette["name"][language],
        "description": palette["description"][language],
        "colors": palette["colors"]
    }

def get_palette_list(language):
    """
    Récupère la liste des palettes disponibles dans la langue spécifiée.

    Args:
        language (str): Code de langue ('fr' ou 'en')

    Returns:
        list: Liste des palettes avec leurs noms et descriptions dans la langue spécifiée
    """
    return [
        {
            "id": palette_id,
            "name": info["name"][language],
            "description": info["description"][language]
        }
        for palette_id, info in calming_palettes.items()
    ]

def get_palette_colors(palette_id):
    """
    Récupère les couleurs d'une palette.

    Args:
        palette_id (str): Identifiant de la palette

    Returns:
        dict: Couleurs de la palette
    """
    return calming_palettes.get(palette_id, calming_palettes["default"])["colors"]
