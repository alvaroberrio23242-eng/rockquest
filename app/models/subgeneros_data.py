# app/models/subgeneros_data.py
"""Catalogo de subgeneros del rock. El campo 'genero_match' se usa en
la ruta /subgeneros para buscar, por texto, bandas de la BD cuyo
campo Banda.genero lo mencione -- asi no hay que mantener una lista
de 'bandas representativas' a mano y desincronizada de la BD real."""

SUBGENEROS = [
    {
        "slug": "rock-and-roll",
        "nombre": "Rock and Roll",
        "decada_origen": "1950s",
        "genero_match": "Rock and Roll",
        "descripcion": (
            "El género fundacional. Nace de la fusión del blues, el "
            "country y el rhythm & blues, con Chuck Berry, Elvis Presley "
            "y Little Richard como sus figuras pioneras."
        ),
    },
    {
        "slug": "rockabilly",
        "nombre": "Rockabilly",
        "decada_origen": "1950s",
        "genero_match": "Rockabilly",
        "descripcion": (
            "Mezcla el rock and roll temprano con el country 'hillbilly' "
            "sureño de EE. UU. Guitarras eléctricas rápidas y un pulso "
            "rítmico prestado del country tradicional."
        ),
    },
    {
        "slug": "british-invasion",
        "nombre": "British Invasion",
        "decada_origen": "1960s",
        "genero_match": "British Invasion",
        "descripcion": (
            "El nombre que se le dio al fenómeno de bandas británicas -"
            "encabezadas por The Beatles- conquistando las listas "
            "estadounidenses a mediados de los 60."
        ),
    },
    {
        "slug": "rock-psicodelico",
        "nombre": "Rock Psicodélico",
        "decada_origen": "1960s",
        "genero_match": "Psicodélico",
        "descripcion": (
            "Busca replicar musicalmente experiencias alteradas de la "
            "conciencia: efectos de estudio experimentales, estructuras "
            "no convencionales y letras surrealistas."
        ),
    },
    {
        "slug": "folk-rock",
        "nombre": "Folk Rock",
        "decada_origen": "1960s",
        "genero_match": "Folk Rock",
        "descripcion": (
            "Une la tradición lírica y acústica del folk con "
            "instrumentación eléctrica de rock, muchas veces con "
            "contenido de crítica social o política."
        ),
    },
    {
        "slug": "hard-rock",
        "nombre": "Hard Rock",
        "decada_origen": "1970s",
        "genero_match": "Hard Rock",
        "descripcion": (
            "Guitarras distorsionadas, ritmos contundentes y actitud "
            "agresiva. Sienta las bases directas de las que después "
            "surgirá el heavy metal."
        ),
    },
    {
        "slug": "rock-progresivo",
        "nombre": "Rock Progresivo",
        "decada_origen": "1970s",
        "genero_match": "Rock Progresivo",
        "descripcion": (
            "Estructuras extensas y complejas, influencia del jazz y la "
            "música clásica, y álbumes conceptuales de principio a fin, "
            "en vez de colecciones de canciones sueltas."
        ),
    },
    {
        "slug": "glam-rock",
        "nombre": "Glam Rock",
        "decada_origen": "1970s",
        "genero_match": "Glam Rock",
        "descripcion": (
            "Estética teatral y andrógina, maquillaje, brillo y "
            "espectáculo visual como parte central de la propuesta, no "
            "solo la música."
        ),
    },
    {
        "slug": "punk",
        "nombre": "Punk",
        "decada_origen": "1970s",
        "genero_match": "Punk",
        "descripcion": (
            "Canciones cortas, rápidas y sin adornos, como reacción "
            "directa contra la complejidad del rock progresivo. Actitud "
            "de 'hazlo tú mismo' (DIY) por encima del virtuosismo técnico."
        ),
    },
    {
        "slug": "heavy-metal",
        "nombre": "Heavy Metal",
        "decada_origen": "1980s",
        "genero_match": "Heavy Metal",
        "descripcion": (
            "Lleva la distorsión, el volumen y la velocidad del hard "
            "rock al extremo, con temáticas más oscuras y una técnica "
            "instrumental cada vez más exigente."
        ),
    },
    {
        "slug": "glam-metal",
        "nombre": "Glam Metal",
        "decada_origen": "1980s",
        "genero_match": "Glam Metal",
        "descripcion": (
            "También llamado 'hair metal': combina la agresividad del "
            "heavy metal con la estética visual llamativa del glam rock. "
            "Dominó las radios y MTV durante buena parte de los 80."
        ),
    },
    {
        "slug": "new-wave",
        "nombre": "New Wave",
        "decada_origen": "1980s",
        "genero_match": "New Wave",
        "descripcion": (
            "Surge de la escena punk pero incorpora sintetizadores y una "
            "sensibilidad más pop y bailable, muy ligado a la estética "
            "visual de la era MTV."
        ),
    },
    {
        "slug": "grunge",
        "nombre": "Grunge",
        "decada_origen": "1990s",
        "genero_match": "Grunge",
        "descripcion": (
            "Nacido en Seattle, mezcla la crudeza del punk con riffs de "
            "hard rock y letras introspectivas. Nirvana lo lleva al "
            "mainstream y termina de un golpe con el reinado del glam "
            "metal."
        ),
    },
    {
        "slug": "rock-alternativo",
        "nombre": "Rock Alternativo",
        "decada_origen": "1990s",
        "genero_match": "Rock Alternativo",
        "descripcion": (
            "Paraguas amplio para bandas que se apartan del sonido "
            "comercial dominante de cada época; en los 90 se vuelve, "
            "paradójicamente, la corriente más popular de todas."
        ),
    },
    {
        "slug": "britpop",
        "nombre": "Britpop",
        "decada_origen": "1990s",
        "genero_match": "Britpop",
        "descripcion": (
            "Respuesta británica al grunge estadounidense: melodías más "
            "pegadizas, orgullo nacional explícito e influencia directa "
            "del rock británico de los 60."
        ),
    },
    {
        "slug": "indie-rock",
        "nombre": "Indie Rock",
        "decada_origen": "2000s",
        "genero_match": "Indie Rock",
        "descripcion": (
            "Producción más cruda y autogestionada, muchas veces por "
            "fuera de las grandes discográficas, con enfoque en la "
            "autenticidad por encima de la producción pulida."
        ),
    },
    {
        "slug": "garage-rock-revival",
        "nombre": "Garage Rock Revival",
        "decada_origen": "2000s",
        "genero_match": "Garage Rock",
        "descripcion": (
            "Vuelta al sonido crudo y directo del garage rock de los "
            "60, como reacción al pop y al nu metal muy producidos de "
            "fines de los 90."
        ),
    },
    {
        "slug": "nu-metal",
        "nombre": "Nu Metal",
        "decada_origen": "2000s",
        "genero_match": "Nu Metal",
        "descripcion": (
            "Combina el peso del metal con elementos de hip hop, "
            "grunge e industrial. Dominó las radios de rock a fines de "
            "los 90 y principios de los 2000."
        ),
    },
    {
        "slug": "pop-punk",
        "nombre": "Pop Punk",
        "decada_origen": "2000s",
        "genero_match": "Pop Punk",
        "descripcion": (
            "Estructuras pegadizas de pop sobre la energía y velocidad "
            "del punk. Muy ligado a la estética y cultura emo de la "
            "década de 2000."
        ),
    },
]
