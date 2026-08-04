# app/models/trivia_data.py
"""Banco de preguntas para la trivia. Todas se basan en contenido que
ya existe en otras secciones del sitio (decadas, subgeneros, linea
del tiempo, bandas y artistas), para no inventar datos sueltos."""

PREGUNTAS = [
    {
        "pregunta": "¿En qué año lanzó Nirvana el álbum 'Nevermind'?",
        "opciones": ["1989", "1991", "1994"],
        "correcta": 1,
    },
    {
        "pregunta": "¿Qué banda es la referente del rock progresivo en RockQuest?",
        "opciones": ["Led Zeppelin", "Pink Floyd", "Queen"],
        "correcta": 1,
    },
    {
        "pregunta": "¿Cuál era el instrumento principal de Robert Plant?",
        "opciones": ["Guitarra", "Batería", "Voz"],
        "correcta": 2,
    },
    {
        "pregunta": "¿En qué década nació el punk como género?",
        "opciones": ["1960s", "1970s", "1980s"],
        "correcta": 1,
    },
    {
        "pregunta": "¿Qué canal, lanzado en 1981, cambió la industria musical con el video?",
        "opciones": ["VH1", "MTV", "BBC"],
        "correcta": 1,
    },
    {
        "pregunta": "¿Qué banda popularizó el grunge a nivel mundial?",
        "opciones": ["Pearl Jam", "Soundgarden", "Nirvana"],
        "correcta": 2,
    },
    {
        "pregunta": "¿Quién fue el vocalista y pianista de Queen?",
        "opciones": ["Freddie Mercury", "Brian May", "John Deacon"],
        "correcta": 0,
    },
    {
        "pregunta": "¿Qué festival de 1969 se volvió símbolo de la contracultura rockera?",
        "opciones": ["Live Aid", "Woodstock", "Monterey Pop"],
        "correcta": 1,
    },
    {
        "pregunta": "¿Qué subgénero combina el peso del metal con hip hop e industrial?",
        "opciones": ["Glam Metal", "Nu Metal", "Rock Alternativo"],
        "correcta": 1,
    },
    {
        "pregunta": "¿En qué año debutó The Beatles en el Ed Sullivan Show?",
        "opciones": ["1962", "1964", "1967"],
        "correcta": 1,
    },
]
