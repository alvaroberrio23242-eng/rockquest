# app/models/historia_data.py
"""Capitulos del relato general de la historia del rock (pagina /historia).
Solo hechos ampliamente documentados; el detalle por decada vive en
decadas_data.py y los hitos puntuales en linea_tiempo_data.py."""

CAPITULOS = [
    {
        "slug": "raices",
        "titulo": "Las raíces",
        "rango": "Antes de 1950",
        "texto": (
            "El rock no nace de la nada: surge del cruce entre el blues y el "
            "gospel afroamericanos, el country del sur de Estados Unidos y el "
            "rhythm & blues de las ciudades. Esa mezcla, cocinada durante "
            "décadas, es la materia prima del rock and roll."
        ),
        "destacados": ["Blues", "Gospel", "Country", "Rhythm & Blues"],
    },
    {
        "slug": "rock-and-roll",
        "titulo": "Nace el rock and roll",
        "rango": "1950 – 1959",
        "texto": (
            "A mediados de los 50 el género llega al público masivo. Bill "
            "Haley graba 'Rock Around the Clock' en 1954, Chuck Berry y "
            "Little Richard definen el sonido de la guitarra y el piano, y "
            "Elvis Presley graba en Sun Records, en Memphis, y se convierte "
            "en el rostro del fenómeno."
        ),
        "destacados": ["Elvis Presley", "Chuck Berry", "Little Richard", "Bill Haley"],
    },
    {
        "slug": "invasion-britanica",
        "titulo": "Invasión Británica y contracultura",
        "rango": "1960 – 1969",
        "texto": (
            "En 1964 The Beatles llegan a Estados Unidos y detonan la "
            "'Invasión Británica', con The Rolling Stones y The Who detrás. "
            "El rock se vuelve experimental y psicodélico, y el Festival de "
            "Woodstock (1969) se convierte en símbolo de toda una época."
        ),
        "destacados": ["The Beatles", "The Rolling Stones", "The Who", "Woodstock"],
    },
    {
        "slug": "hard-rock-punk",
        "titulo": "Hard rock, progresivo y punk",
        "rango": "1970 – 1979",
        "texto": (
            "Led Zeppelin y Black Sabbath endurecen el sonido, Pink Floyd y "
            "otras bandas llevan el rock a estructuras largas y conceptuales, "
            "y Queen mezcla teatralidad y virtuosismo. Hacia 1976, Ramones "
            "responde con canciones cortas y directas: nace el punk."
        ),
        "destacados": ["Led Zeppelin", "Black Sabbath", "Pink Floyd", "Queen", "Ramones"],
    },
    {
        "slug": "mtv-metal",
        "titulo": "MTV y el metal",
        "rango": "1980 – 1989",
        "texto": (
            "MTV debuta en 1981 y la imagen pasa a pesar tanto como el "
            "sonido. El heavy metal se vuelve masivo con bandas como "
            "Metallica, Guns N' Roses llega al estrellato y U2 llena "
            "estadios. En 1985, Live Aid reúne a los grandes del momento."
        ),
        "destacados": ["MTV", "Metallica", "Guns N' Roses", "U2", "Live Aid"],
    },
    {
        "slug": "grunge-alternativo",
        "titulo": "Grunge y rock alternativo",
        "rango": "1990 – 1999",
        "texto": (
            "'Nevermind' de Nirvana (1991) pone al grunge de Seattle en el "
            "centro de la escena, junto a Pearl Jam. El rock alternativo se "
            "vuelve corriente dominante y, en el Reino Unido, el Britpop con "
            "Oasis y Blur renueva el orgullo del rock británico."
        ),
        "destacados": ["Nirvana", "Pearl Jam", "Oasis", "Blur"],
    },
    {
        "slug": "revival-digital",
        "titulo": "Revival y era digital",
        "rango": "2000 – hoy",
        "texto": (
            "The Strokes y The White Stripes traen de vuelta el sonido "
            "crudo del garage rock, mientras bandas como Foo Fighters "
            "sostienen el rock de estadio. Internet y el streaming cambian "
            "por completo cómo se descubre y se escucha el rock."
        ),
        "destacados": ["The Strokes", "The White Stripes", "Foo Fighters"],
    },
    {
        "slug": "medellin",
        "titulo": "El rock en Medellín y Antioquia",
        "rango": "1971 – hoy",
        "texto": (
            "Antioquia tiene su propia historia rockera. El Festival de "
            "Ancón (1971), en La Estrella, es uno de los hitos del rock "
            "colombiano. Décadas después, la escena sigue viva en bares y "
            "escenarios, y MUROCK, el museo del rock de Medellín, preserva "
            "esa memoria."
        ),
        "destacados": ["Festival de Ancón", "MUROCK", "Ciudad Altavoz"],
        "enlace": {"texto": "Ver la Ruta Rockera", "href": "/ruta-rockera"},
    },
]