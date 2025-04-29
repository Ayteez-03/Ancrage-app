"""
Module contenant les traductions pour l'application d'ancrage psychothérapeutique.
"""

# Traductions pour les éléments d'interface générale
ui_translations = {
    "fr": {
        "app_title": "Programme d'Ancrage Psychothérapeutique",
        "start_button": "Commencer le questionnaire",
        "next_button": "Suivant",
        "back_button": "Retour",
        "restart_button": "Recommencer le questionnaire",
        "more_info_button": "En savoir plus sur la méthodologie",
        "success_box_button": "En savoir plus sur la boîte à réussites",
        "back_to_results": "Retour aux résultats",
        "question_progress": "Question {current} sur {total}",
        "recommendation_intro": "Basé sur vos réponses, nous vous recommandons:",
        "language_selector": "Langue / Language",
        "color_palette_title": "Palette de couleurs",
        "color_palette_description": "Choisissez une palette de couleurs apaisante pour personnaliser votre expérience",
        "apply_button": "Appliquer",
        "preview_text": "Aperçu",
        "settings_title": "Paramètres",
        "appearance_title": "Apparence",
        "journal_button": "📖 Journal de progrès",
        "journal_title": "Journal de Progrès d'Ancrage",
        "statistics": "Statistiques",
        "engagement": "Engagement",
        "consecutive_days": "jours consécutifs",
        "average_improvement": "Amélioration moyenne",
        "points": "points",
        "add_entry": "Ajouter une entrée",
        "date": "Date",
        "sud_before": "SUD* avant (0-10)",
        "sud_after": "SUD* après (0-10)",
        "sud_explanation": "*SUD = Niveau de perturbation subjectif",
        "context": "Contexte ou situation",
        "technique_used": "Technique utilisée",
        "notes": "Notes ou observations",
        "add_to_journal": "Ajouter au journal",
        "entry_added": "Entrée ajoutée avec succès",
        "my_journal": "Mes entrées de journal",
        "empty_journal": "Votre journal est vide. Ajoutez votre première entrée ci-dessus!",
        "visualization": "Visualisation",
        "evolution_sud": "Évolution des niveaux de perturbation (SUD)",
        "sud_full_explanation": "Niveau de perturbation subjectif, entre 0 et 10. 0 étant \"pas du tout perturbé\" et 10 \"extrêmement perturbé\"",
        "back_to_home": "Retour à l'accueil",
        "before": "avant",
        "after": "après",
        # Authentification
        "login_title": "Connexion à votre journal",
        "login_desc": "Pour sauvegarder votre journal entre les sessions, veuillez vous connecter ou créer un compte. Vos données resteront privées et associées à votre compte.",
        "login_tab": "Connexion",
        "register_tab": "Inscription",
        "username": "Nom d'utilisateur",
        "password": "Mot de passe",
        "confirm_password": "Confirmer le mot de passe",
        "login_button": "Se connecter",
        "register_button": "S'inscrire",
        "logout_button": "Déconnexion",
        "login_success": "Connexion réussie !",
        "register_success": "Inscription réussie, vous pouvez maintenant vous connecter",
        "login_error": "Nom d'utilisateur ou mot de passe incorrect",
        "register_error": "Ce nom d'utilisateur existe déjà",
        "password_mismatch": "Les mots de passe ne correspondent pas",
        "fields_required": "Veuillez remplir tous les champs",
        "logged_in_as": "Connecté en tant que {username}",
        "autosave": "Votre journal est automatiquement sauvegardé.",
        "guest_mode": "Mode invité",
        "guest_warning": "En mode invité, votre journal sera perdu si vous fermez cette page ou actualisez le navigateur.",
        "login_required": "Pour sauvegarder votre journal entre les sessions, veuillez vous connecter.",
        # Audio
        "ambient_sound": "Son d'ambiance",
        "ambient_sound_desc": "Son apaisant pour faciliter l'ancrage",
        "play_sound": "Activer le son apaisant",
        "mute_sound": "Désactiver le son"
    },
    "en": {
        "app_title": "Psychotherapeutic Grounding Program",
        "start_button": "Start questionnaire",
        "next_button": "Next",
        "back_button": "Back",
        "restart_button": "Restart questionnaire",
        "more_info_button": "Learn more about methodology",
        "success_box_button": "Learn more about the success box",
        "back_to_results": "Back to results",
        "question_progress": "Question {current} of {total}",
        "recommendation_intro": "Based on your answers, we recommend:",
        "language_selector": "Language / Langue",
        "color_palette_title": "Color Palette",
        "color_palette_description": "Choose a calming color palette to customize your experience",
        "apply_button": "Apply",
        "preview_text": "Preview",
        "settings_title": "Settings",
        "appearance_title": "Appearance",
        "journal_button": "📖 Progress Journal",
        "journal_title": "Grounding Progress Journal",
        "statistics": "Statistics",
        "engagement": "Engagement",
        "consecutive_days": "consecutive days",
        "average_improvement": "Average improvement",
        "points": "points",
        "add_entry": "Add an entry",
        "date": "Date",
        "sud_before": "SUD* before (0-10)",
        "sud_after": "SUD* after (0-10)",
        "sud_explanation": "*SUD = Subjective units of distress",
        "context": "Context or situation",
        "technique_used": "Technique used",
        "notes": "Notes or observations",
        "add_to_journal": "Add to journal",
        "entry_added": "Entry added successfully",
        "my_journal": "My journal entries",
        "empty_journal": "Your journal is empty. Add your first entry above!",
        "visualization": "Visualization",
        "evolution_sud": "Evolution of distress levels (SUD)",
        "sud_full_explanation": "Subjective units of distress, between 0 and 10. 0 being \"not disturbed at all\" and 10 \"extremely disturbed\"",
        "back_to_home": "Back to home",
        "before": "before",
        "after": "after",
        # Authentication
        "login_title": "Journal Login",
        "login_desc": "To save your journal between sessions, please log in or create an account. Your data will remain private and associated with your account.",
        "login_tab": "Login",
        "register_tab": "Register",
        "username": "Username",
        "password": "Password",
        "confirm_password": "Confirm password",
        "login_button": "Login",
        "register_button": "Register",
        "logout_button": "Logout",
        "login_success": "Login successful!",
        "register_success": "Registration successful, you can now log in",
        "login_error": "Incorrect username or password",
        "register_error": "This username already exists",
        "password_mismatch": "Passwords do not match",
        "fields_required": "Please fill in all fields",
        "logged_in_as": "Logged in as {username}",
        "autosave": "Your journal is automatically saved.",
        "guest_mode": "Guest mode",
        "guest_warning": "In guest mode, your journal will be lost if you close this page or refresh the browser.",
        "login_required": "To save your journal between sessions, please log in.",
        # Audio
        "ambient_sound": "Ambient Sound",
        "ambient_sound_desc": "Calming sound to aid grounding",
        "play_sound": "Play calming sound",
        "mute_sound": "Mute sound"
    }
}

# Traductions pour la page d'accueil
welcome_translations = {
    "fr": {
        "title": "Programme d'Ancrage Psychothérapeutique",
        "welcome_text": "Bienvenue dans ce programme d'ancrage psychothérapeutique.",
        "what_is_title": "Qu'est-ce que l'ancrage psychothérapeutique ?",
        "what_is_text": "L'ancrage psychothérapeutique comprend un ensemble de techniques permettant de vous connecter "
                      "au moment présent, particulièrement utiles lors de situations de stress, d'anxiété ou lorsque vous êtes "
                      "submergé(e) par des émotions intenses.",
        "about_questionnaire_title": "À propos de ce questionnaire",
        "about_questionnaire_text": "Ce questionnaire vous aidera à identifier les techniques d'ancrage qui sont les plus adaptées à votre "
                                  "profil personnel. En répondant à quelques questions simples, nous pourrons vous recommander des "
                                  "exercices d'ancrage personnalisés que vous pourrez utiliser dans votre quotidien.",
        "ready_text": "Prêt(e) à commencer ?"
    },
    "en": {
        "title": "Psychotherapeutic Grounding Program",
        "welcome_text": "Welcome to this psychotherapeutic grounding program.",
        "what_is_title": "What is psychotherapeutic grounding?",
        "what_is_text": "Psychotherapeutic grounding includes a set of techniques that help you connect "
                      "to the present moment, particularly useful in situations of stress, anxiety, or when you feel "
                      "overwhelmed by intense emotions.",
        "about_questionnaire_title": "About this questionnaire",
        "about_questionnaire_text": "This questionnaire will help you identify the grounding techniques that are most suitable for your "
                                  "personal profile. By answering a few simple questions, we can recommend "
                                  "personalized grounding exercises that you can use in your daily life.",
        "ready_text": "Ready to begin?"
    }
}

# Traductions pour la page À propos
about_translations = {
    "fr": {
        "title": "À propos des techniques d'ancrage",
        "methodology_title": "Méthodologie",
        "methodology_text": "Les techniques d'ancrage sont des outils thérapeutiques fondés sur des principes de thérapie cognitive-comportementale, "
                          "de pleine conscience et d'autres approches psychologiques validées scientifiquement.",
        "questionnaire_eval": "Le questionnaire que vous avez complété évalue votre affinité avec trois types principaux de techniques d'ancrage :",
        "body_techniques": "**Techniques centrées sur le corps** : Utilisent les sensations physiques comme point d'ancrage.",
        "orientation_techniques": "**Techniques centrées sur l'orientation** : Utilisent l'environnement extérieur comme point d'ancrage.",
        "imagination_techniques": "**Techniques centrées sur l'imagination** : Utilisent des visualisations et pensées pour créer un ancrage.",
        "effectiveness_title": "Efficacité",
        "effectiveness_text": "L'efficacité des techniques d'ancrage varie d'une personne à l'autre. Certaines personnes répondent mieux aux techniques "
                            "corporelles, d'autres aux techniques visuelles ou cognitives. C'est pourquoi une approche personnalisée est importante.",
        "useful_for": "Les techniques d'ancrage sont particulièrement utiles pour :",
        "useful_anxiety": "Gérer l'anxiété",
        "useful_ptsd": "Réduire les symptômes de stress post-traumatique",
        "useful_dissociation": "Rester présent lors de moments de dissociation",
        "useful_panic": "Gérer les crises de panique",
        "useful_emotions": "Réguler les émotions intenses",
        "regular_practice_title": "Pratique régulière",
        "regular_practice_text": "Pour une efficacité optimale, il est recommandé de pratiquer ces techniques régulièrement, même lorsque vous vous "
                               "sentez bien. Cela permet de les maîtriser et de pouvoir les utiliser plus facilement dans des moments difficiles."
    },
    "en": {
        "title": "About Grounding Techniques",
        "methodology_title": "Methodology",
        "methodology_text": "Grounding techniques are therapeutic tools based on principles of cognitive-behavioral therapy, "
                          "mindfulness, and other scientifically validated psychological approaches.",
        "questionnaire_eval": "The questionnaire you completed evaluates your affinity with three main types of grounding techniques:",
        "body_techniques": "**Body-centered techniques**: Use physical sensations as an anchor point.",
        "orientation_techniques": "**Orientation-centered techniques**: Use the external environment as an anchor point.",
        "imagination_techniques": "**Imagination-centered techniques**: Use visualizations and thoughts to create an anchor.",
        "effectiveness_title": "Effectiveness",
        "effectiveness_text": "The effectiveness of grounding techniques varies from person to person. Some people respond better to "
                            "physical techniques, others to visual or cognitive techniques. That's why a personalized approach is important.",
        "useful_for": "Grounding techniques are particularly useful for:",
        "useful_anxiety": "Managing anxiety",
        "useful_ptsd": "Reducing symptoms of post-traumatic stress",
        "useful_dissociation": "Staying present during moments of dissociation",
        "useful_panic": "Managing panic attacks",
        "useful_emotions": "Regulating intense emotions",
        "regular_practice_title": "Regular Practice",
        "regular_practice_text": "For optimal effectiveness, it is recommended to practice these techniques regularly, even when you "
                               "feel well. This allows you to master them and be able to use them more easily in difficult moments."
    }
}

# Traductions pour la page de la boîte à réussites
success_box_translations = {
    "fr": {
        "title": "🧠 La Boîte à Réussites",
        "how_it_works_title": "Comment ça fonctionne ?",
        "how_it_works_text": "Tu vas imaginer (ou créer en vrai) une boîte spéciale dans laquelle tu \"ranges\" des souvenirs, objets, pensées ou symboles qui te rappellent :",
        "achievements": "Tes réussites passées (même petites).",
        "positive_moments": "Les moments où tu t'es senti(e) fier/fière, heureux(se), capable, aimé(e), apaisé(e), etc.",
        "compliments": "Des compliments qu'on t'a faits.",
        "mental_images": "Des images mentales positives, comme un lieu refuge ou une lumière protectrice.",
        "practice_title": "Deux façons de la pratiquer :",
        "imagination_title": "🔹 En imagination uniquement (mentalement) :",
        "imagination_step1": "Ferme les yeux.",
        "imagination_step2": "Imagine une boîte à ton goût (taille, forme, matière).",
        "imagination_step3": "Visualise que tu y mets des souvenirs positifs : par exemple, ton diplôme, un sourire reçu, une victoire personnelle.",
        "imagination_step4": "Chaque fois que tu en as besoin, imagine que tu l'ouvres pour y puiser de la force.",
        "physical_title": "🔹 En vrai (physiquement) :",
        "physical_step1": "Prends une vraie boîte ou une boîte virtuelle (notes dans ton téléphone, carnet, etc).",
        "physical_step2": "Mets-y des objets symboliques : photos, mots, dessins, citations, lettres, objets qui t'apaisent ou te rappellent ta valeur.",
        "physical_step3": "Reviens y jeter un œil régulièrement, surtout dans les moments difficiles."
    },
    "en": {
        "title": "🧠 The Success Box",
        "how_it_works_title": "How does it work?",
        "how_it_works_text": "You will imagine (or create for real) a special box in which you \"store\" memories, objects, thoughts, or symbols that remind you of:",
        "achievements": "Your past achievements (even small ones).",
        "positive_moments": "Moments when you felt proud, happy, capable, loved, peaceful, etc.",
        "compliments": "Compliments you've received.",
        "mental_images": "Positive mental images, such as a safe place or a protective light.",
        "practice_title": "Two ways to practice it:",
        "imagination_title": "🔹 In imagination only (mentally):",
        "imagination_step1": "Close your eyes.",
        "imagination_step2": "Imagine a box to your liking (size, shape, material).",
        "imagination_step3": "Visualize putting positive memories in it: for example, your diploma, a smile you received, a personal victory.",
        "imagination_step4": "Whenever you need it, imagine opening it to draw strength.",
        "physical_title": "🔹 In reality (physically):",
        "physical_step1": "Take a real box or a virtual box (notes in your phone, notebook, etc.).",
        "physical_step2": "Put symbolic objects in it: photos, words, drawings, quotes, letters, objects that soothe you or remind you of your worth.",
        "physical_step3": "Come back to look at it regularly, especially during difficult times."
    }
}

# Traductions pour les questions
questions_translations = {
    "fr": [
        ("Êtes-vous à l'aise avec les yeux fermés ?", ["Oui", "Non", "Pas sûr(e)"]),
        ("Comment vous sentez-vous par rapport à vos sensations corporelles ?", ["Je suis très connecté(e) à mon corps.", "Je suis un peu connecté(e) à mes sensations corporelles.", "Je suis rarement conscient(e) de mes sensations corporelles."]),
        ("Quand vous êtes confronté(e) à des situations émotionnelles, vous vous concentrez davantage sur :", ["Ce que je ressens dans mon corps.", "Ce qui se passe autour de moi (mon environnement).", "Mes pensées et images mentales."]),
        ("Préférez-vous des exercices physiques comme la marche, le vélo, ou les étirements pour vous détendre ?", ["Oui, cela m'aide beaucoup.", "Pas vraiment, mais j'essaie de temps en temps.", "Non, je préfère éviter l'activité physique."]),
        ("Comment êtes-vous avec les souvenirs ou les imaginations ?", ["Je peux facilement visualiser des souvenirs agréables.", "J'ai du mal à visualiser des souvenirs, mais j'aime imaginer des histoires.", "Je ne suis pas très à l'aise avec l'imagination."]),
        ("Comment réagissez-vous aux distractions autour de vous ?", ["Je me laisse facilement distraire.", "Je suis assez concentré(e), mais je peux être distrait(e) parfois.", "Je reste généralement très concentré(e)."]),
        ("Avez-vous une préférence pour vous concentrer sur des éléments précis dans votre environnement (ex : couleurs, sons, textures) lorsque vous êtes perturbé(e) ?", ["Oui, cela m'aide à revenir dans l'instant présent.", "Je m'en soucie un peu, mais pas trop.", "Non, je ne prête pas attention aux éléments autour de moi."])
    ],
    "en": [
        ("Are you comfortable with your eyes closed?", ["Yes", "No", "Not sure"]),
        ("How do you feel about your bodily sensations?", ["I am very connected to my body.", "I am somewhat connected to my bodily sensations.", "I am rarely aware of my bodily sensations."]),
        ("When confronted with emotional situations, you focus more on:", ["What I feel in my body.", "What is happening around me (my environment).", "My thoughts and mental images."]),
        ("Do you prefer physical exercises like walking, cycling, or stretching to relax?", ["Yes, it helps me a lot.", "Not really, but I try sometimes.", "No, I prefer to avoid physical activity."]),
        ("How are you with memories or imaginations?", ["I can easily visualize pleasant memories.", "I have trouble visualizing memories, but I like imagining stories.", "I am not very comfortable with imagination."]),
        ("How do you react to distractions around you?", ["I get easily distracted.", "I am quite focused, but can be distracted sometimes.", "I usually stay very focused."]),
        ("Do you have a preference for focusing on specific elements in your environment (e.g., colors, sounds, textures) when you're upset?", ["Yes, it helps me return to the present moment.", "I care a little, but not too much.", "No, I don't pay attention to elements around me."])
    ]
}

# Traductions pour les techniques d'ancrage
techniques_translations = {
    "fr": {
        "Techniques d'ancrage centrées sur le corps": """
        ## Techniques d'ancrage centrées sur le corps
        
        Ces techniques utilisent les sensations physiques pour vous aider à rester présent(e).
        
        ### Exercices recommandés:
        
        1. **Respiration consciente**: Concentrez-vous sur votre respiration. Sentez l'air entrer et sortir de vos poumons.
        
        2. **Scan corporel**: Portez attention à chaque partie de votre corps, en commençant par les orteils et en remontant progressivement.
        
        3. **Ancrage par les pieds**: Sentez le contact de vos pieds avec le sol. Concentrez-vous sur cette sensation pour revenir au présent.
        
        4. **Contraction-relaxation musculaire**: Contractez puis relâchez progressivement différents groupes musculaires.
        
        5. **Eau froide sur le visage**: Appliquez de l'eau froide sur votre visage pour créer une sensation physique forte qui vous ramène au présent.
        
        Ces techniques sont particulièrement efficaces pour les personnes qui sont bien connectées à leurs sensations corporelles.
        
        ---
        
        > ### Exemples de techniques
        > 
        > - Je m'étire fort (doigts, bras, muscles du visage, jambes, dos, épaules, etc)
        > - Je serre les poings, je les desserre en me concentrant dessus
        > - Je fais de l'exercice (marche, course, vélo, etc)

        """,
        
        "Techniques d'ancrage centrées sur l'orientation": """
        ## Techniques d'ancrage centrées sur l'orientation
        
        Ces techniques utilisent votre environnement pour vous aider à retrouver votre stabilité émotionnelle.
        
        ### Exercices recommandés:
        
        1. **Technique des 5-4-3-2-1**: Identifiez:
           - 5 choses que vous pouvez voir
           - 4 choses que vous pouvez toucher
           - 3 choses que vous pouvez entendre
           - 2 choses que vous pouvez sentir
           - 1 chose que vous pouvez goûter
        
        2. **Focalisation sur un objet**: Choisissez un objet dans votre environnement et décrivez-le en détail (couleur, texture, forme, etc.).
        
        3. **Nommer les objets**: Nommez tous les objets d'une certaine couleur dans votre environnement.
        
        4. **Concentration sur les sons**: Identifiez tous les sons différents que vous pouvez entendre.
        
        5. **Ancrage spatial**: Prenez conscience de l'espace autour de vous, de la position de votre corps dans cet espace.
        
        Ces techniques sont particulièrement efficaces pour les personnes qui préfèrent rester connectées à leur environnement.
        
        ---
        
        > ### Exemples de techniques
        > 
        > - Je nomme le lieu dans lequel je suis ainsi que l'heure et la date (par exemple : je suis dans un parc, il est 14h et nous sommes le 14 Janvier)

        """,
        
        "Techniques d'ancrage centrées sur l'imagination": """
        ## Techniques d'ancrage centrées sur l'imagination
        
        Ces techniques utilisent votre imagination et votre pensée pour vous aider à retrouver votre calme et votre stabilité.
        
        ### Exercices recommandés:
        
        1. **Lieu sûr imaginaire**: Visualisez un endroit où vous vous sentez complètement en sécurité et en paix.
        
        2. **Visualisation positive**: Imaginez une scène où vous vous sentez calme, confiant(e) et en contrôle.
        
        3. **Récitation mentale**: Récitez mentalement un poème, des paroles de chanson ou un mantra apaisant.
        
        4. **Dialogue interne positif**: Utilisez des affirmations positives comme "Je suis en sécurité maintenant" ou "Je peux gérer cette situation".
        
        5. **Technique de distraction cognitive**: Faites un calcul mental, récitez l'alphabet à l'envers, ou pensez à des mots commençant par chaque lettre de l'alphabet.
        
        Ces techniques sont particulièrement efficaces pour les personnes qui ont une imagination vive et qui trouvent du réconfort dans la pensée et la visualisation.
        
        ---
        
        > ### Exemples de techniques
        > 
        > - Je décris en détails un souvenir neutre ou agréable
        > - Je m'imagine être protégé(e) par des barrières, un pouvoir, etc.
        > - Je me crée (en imaginaire ou en réel) une boîte à réussites

        """,
        
        "Mélange de techniques": """
        ## Mélange de techniques d'ancrage
        
        Selon vos réponses, vous pourriez bénéficier d'une approche mixte, combinant différentes techniques d'ancrage.
        
        ### Suggestions:
        
        1. **Combinaison corps-orientation**:
           - Sentez vos pieds sur le sol tout en nommant cinq objets que vous voyez autour de vous.
           - Faites des exercices de respiration tout en vous concentrant sur les sons de votre environnement.
        
        2. **Combinaison corps-imagination**:
           - Pratiquez la respiration consciente tout en visualisant un lieu sûr.
           - Utilisez le scan corporel tout en vous répétant des affirmations positives.
        
        3. **Combinaison orientation-imagination**:
           - Observez votre environnement tout en construisant une histoire positive autour de ce que vous voyez.
           - Concentrez-vous sur un objet et imaginez son histoire ou son origine.
        
        4. **Approche flexible**:
           - Essayez différentes techniques selon les situations et votre état émotionnel du moment.
           - Tenez un journal pour noter quelles techniques fonctionnent le mieux pour vous dans différents contextes.
        
        L'avantage d'une approche mixte est sa flexibilité - vous pouvez adapter vos stratégies d'ancrage selon les circonstances et vos besoins du moment.
        

        """
    },
    "en": {
        "Body-centered grounding techniques": """
        ## Body-centered grounding techniques
        
        These techniques use physical sensations to help you stay present.
        
        ### Recommended exercises:
        
        1. **Conscious breathing**: Focus on your breathing. Feel the air entering and leaving your lungs.
        
        2. **Body scan**: Pay attention to each part of your body, starting with your toes and gradually moving upward.
        
        3. **Feet grounding**: Feel the contact of your feet with the ground. Focus on this sensation to return to the present.
        
        4. **Muscle contraction-relaxation**: Contract then gradually release different muscle groups.
        
        5. **Cold water on face**: Apply cold water to your face to create a strong physical sensation that brings you back to the present.
        
        These techniques are particularly effective for people who are well connected to their bodily sensations.
        
        ---
        
        > ### Example techniques
        > 
        > - I stretch strongly (fingers, arms, facial muscles, legs, back, shoulders, etc.)
        > - I clench my fists, then release them while focusing on the sensation
        > - I exercise (walking, running, cycling, etc.)

        """,
        
        "Orientation-centered grounding techniques": """
        ## Orientation-centered grounding techniques
        
        These techniques use your environment to help you regain your emotional stability.
        
        ### Recommended exercises:
        
        1. **5-4-3-2-1 Technique**: Identify:
           - 5 things you can see
           - 4 things you can touch
           - 3 things you can hear
           - 2 things you can smell
           - 1 thing you can taste
        
        2. **Object focus**: Choose an object in your environment and describe it in detail (color, texture, shape, etc.).
        
        3. **Naming objects**: Name all objects of a certain color in your environment.
        
        4. **Sound concentration**: Identify all the different sounds you can hear.
        
        5. **Spatial anchoring**: Be aware of the space around you, the position of your body in this space.
        
        These techniques are particularly effective for people who prefer to stay connected to their environment.
        
        ---
        
        > ### Example techniques
        > 
        > - I name the place where I am as well as the time and date (for example: I am in a park, it is 2 PM and today is January 14)

        """,
        
        "Imagination-centered grounding techniques": """
        ## Imagination-centered grounding techniques
        
        These techniques use your imagination and thinking to help you regain your calm and stability.
        
        ### Recommended exercises:
        
        1. **Imaginary safe place**: Visualize a place where you feel completely safe and at peace.
        
        2. **Positive visualization**: Imagine a scene where you feel calm, confident, and in control.
        
        3. **Mental recitation**: Mentally recite a poem, song lyrics, or a soothing mantra.
        
        4. **Positive internal dialogue**: Use positive affirmations such as "I am safe now" or "I can handle this situation".
        
        5. **Cognitive distraction technique**: Do a mental calculation, recite the alphabet backwards, or think of words starting with each letter of the alphabet.
        
        These techniques are particularly effective for people who have a vivid imagination and find comfort in thinking and visualization.
        
        ---
        
        > ### Example techniques
        > 
        > - I describe in detail a neutral or pleasant memory
        > - I imagine being protected by barriers, a power, etc.
        > - I create (in imagination or in reality) a success box

        """,
        
        "Mix of techniques": """
        ## Mix of grounding techniques
        
        Based on your answers, you might benefit from a mixed approach, combining different grounding techniques.
        
        ### Suggestions:
        
        1. **Body-orientation combination**:
           - Feel your feet on the ground while naming five objects you see around you.
           - Do breathing exercises while focusing on the sounds of your environment.
        
        2. **Body-imagination combination**:
           - Practice conscious breathing while visualizing a safe place.
           - Use body scanning while repeating positive affirmations to yourself.
        
        3. **Orientation-imagination combination**:
           - Observe your environment while building a positive story around what you see.
           - Focus on an object and imagine its history or origin.
        
        4. **Flexible approach**:
           - Try different techniques depending on the situations and your emotional state of the moment.
           - Keep a journal to note which techniques work best for you in different contexts.
        
        The advantage of a mixed approach is its flexibility - you can adapt your grounding strategies according to the circumstances and your needs of the moment.
        

        """
    }
}

# Mapping des noms techniques
technique_name_mapping = {
    "fr": {
        "Techniques d'ancrage centrées sur le corps": "Techniques d'ancrage centrées sur le corps",
        "Techniques d'ancrage centrées sur l'orientation": "Techniques d'ancrage centrées sur l'orientation",
        "Techniques d'ancrage centrées sur l'imagination": "Techniques d'ancrage centrées sur l'imagination",
        "Mélange de techniques": "Mélange de techniques"
    },
    "en": {
        "Techniques d'ancrage centrées sur le corps": "Body-centered grounding techniques",
        "Techniques d'ancrage centrées sur l'orientation": "Orientation-centered grounding techniques",
        "Techniques d'ancrage centrées sur l'imagination": "Imagination-centered grounding techniques",
        "Mélange de techniques": "Mix of techniques"
    }
}
