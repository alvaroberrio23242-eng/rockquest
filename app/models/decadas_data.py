# app/models/decadas_data.py
"""
Contenido narrativo de cada decada del rock. Las bandas reales de
cada decada NO viven aca -- se traen de la tabla Banda (columna
decada_principal) en la ruta /decadas, para no duplicar datos.
"""

DECADAS = [
    {
        "slug": "1950s",
        "nombre": "Los 50",
        "rango_anios": "1950 – 1959",
        "descripcion": (
            "El rock and roll nace de la fusión del blues, el country y el "
            "rhythm & blues afroamericano. Chuck Berry sienta las bases del "
            "riff de guitarra como columna vertebral del género, mientras "
            "Elvis Presley y Little Richard lo llevan al público masivo."
        ),
        "subgeneros": ["Rock and Roll", "Rockabilly"],
    },
    {
        "slug": "1960s",
        "nombre": "Los 60",
        "rango_anios": "1960 – 1969",
        "descripcion": (
            "La 'Invasión Británica' liderada por The Beatles cambia la "
            "industria musical global. El rock se diversifica: aparecen el "
            "folk rock, el rock psicodélico y una conciencia contracultural "
            "que culmina en Woodstock (1969)."
        ),
        "subgeneros": ["British Invasion", "Rock Psicodélico", "Folk Rock"],
    },
    {
        "slug": "1970s",
        "nombre": "Los 70",
        "rango_anios": "1970 – 1979",
        "descripcion": (
            "Década de expansión y extremos: el hard rock y el rock "
            "progresivo llevan la complejidad y el volumen al límite, el "
            "glam rock apuesta por la teatralidad, y hacia el final de la "
            "década el punk aparece como una reacción cruda y directa "
            "contra todo eso."
        ),
        "subgeneros": ["Hard Rock", "Rock Progresivo", "Glam Rock", "Punk"],
    },
    {
        "slug": "1980s",
        "nombre": "Los 80",
        "rango_anios": "1980 – 1989",
        "descripcion": (
            "El heavy metal se vuelve masivo y se ramifica en múltiples "
            "subgéneros. La llegada de MTV en 1981 transforma la industria: "
            "la imagen pasa a ser tan importante como el sonido, impulsando "
            "al glam metal y al new wave."
        ),
        "subgeneros": ["Heavy Metal", "Glam Metal", "New Wave"],
    },
    {
        "slug": "1990s",
        "nombre": "Los 90",
        "rango_anios": "1990 – 1999",
        "descripcion": (
            "El grunge de Seattle, encabezado por Nirvana, termina de un "
            "golpe con el reinado del glam metal e instala al rock "
            "alternativo como corriente dominante. En paralelo, el Britpop "
            "revive el orgullo del rock británico."
        ),
        "subgeneros": ["Grunge", "Rock Alternativo", "Britpop"],
    },
    {
        "slug": "2000s",
        "nombre": "Los 2000",
        "rango_anios": "2000 – 2009",
        "descripcion": (
            "Un revival del garage rock (The Strokes, The White Stripes) "
            "trae de vuelta el sonido crudo y directo, mientras el nu metal "
            "y el pop punk dominan las radios y el emo se convierte en una "
            "identidad cultural completa para toda una generación."
        ),
        "subgeneros": ["Indie Rock", "Garage Rock Revival", "Nu Metal", "Pop Punk"],
    },
]
