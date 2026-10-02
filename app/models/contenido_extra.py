# app/models/contenido_extra.py
"""Ampliacion de la linea del tiempo y de las decadas (2010s y 2020s).
Se suma a HITOS y DECADAS desde linea_tiempo_data.py y decadas_data.py."""

HITOS_EXTRA = [
    {"anio": 1955, "titulo": "Chuck Berry lanza 'Maybellene'",
     "descripcion": "Su primer sencillo une country y rhythm & blues con un riff de guitarra que se volvería la base del rock and roll."},
    {"anio": 1957, "titulo": "Buddy Holly y The Crickets graban 'That'll Be the Day'",
     "descripcion": "Establece el formato de banda de rock con dos guitarras, bajo y batería que seguirían miles de grupos."},
    {"anio": 1965, "titulo": "Bob Dylan toca con banda eléctrica en Newport",
     "descripcion": "Su paso del folk acústico a la guitarra eléctrica en el Festival de Newport divide a su público y abre el camino del folk rock."},
    {"anio": 1967, "titulo": "The Beatles publican 'Sgt. Pepper's Lonely Hearts Club Band'",
     "descripcion": "Un álbum concebido como obra de estudio, no como colección de sencillos, que redefine lo que un disco de rock puede ser."},
    {"anio": 1969, "titulo": "Led Zeppelin lanza su álbum debut",
     "descripcion": "Blues pesado, volumen y virtuosismo: sienta las bases del hard rock que dominaría los años 70."},
    {"anio": 1970, "titulo": "The Beatles se separan",
     "descripcion": "El anuncio de la salida de Paul McCartney cierra la historia de la banda más influyente de los 60."},
    {"anio": 1971, "titulo": "Festival de Ancón, en La Estrella (Antioquia)",
     "descripcion": "Considerado el 'Woodstock colombiano', reúne a miles de jóvenes y se vuelve un hito de la contracultura y el rock del país."},
    {"anio": 1973, "titulo": "Pink Floyd publica 'The Dark Side of the Moon'",
     "descripcion": "Álbum conceptual que permanece durante años en las listas de ventas y se convierte en uno de los más vendidos de la historia."},
    {"anio": 1975, "titulo": "Queen lanza 'Bohemian Rhapsody'",
     "descripcion": "Una canción de seis minutos que mezcla balada, ópera y hard rock, y que su video promocional ayudó a popularizar."},
    {"anio": 1977, "titulo": "Sex Pistols publican 'Never Mind the Bollocks'",
     "descripcion": "El único álbum de estudio de la banda convierte al punk británico en un fenómeno cultural y mediático."},
    {"anio": 1983, "titulo": "Metallica lanza 'Kill 'Em All'",
     "descripcion": "Su debut impulsa el thrash metal, una versión más rápida y agresiva del heavy metal."},
    {"anio": 1986, "titulo": "Primeros miembros del Salón de la Fama del Rock",
     "descripcion": "Chuck Berry, Elvis Presley y otros pioneros son los primeros en ser incluidos en el Rock and Roll Hall of Fame."},
    {"anio": 1987, "titulo": "Guns N' Roses lanza 'Appetite for Destruction'",
     "descripcion": "Un sonido crudo y callejero que contrasta con el glam metal de la época y se vuelve uno de los debuts más vendidos."},
    {"anio": 1994, "titulo": "Oasis lanza 'Definitely Maybe'",
     "descripcion": "Su debut marca el auge del Britpop y relanza el orgullo del rock británico."},
    {"anio": 1997, "titulo": "Radiohead publica 'OK Computer'",
     "descripcion": "Un álbum que explora la tecnología y la alienación y se considera uno de los más influyentes del rock alternativo."},
    {"anio": 2003, "titulo": "The White Stripes lanza 'Seven Nation Army'",
     "descripcion": "Su riff de guitarra, tocado con efectos para sonar como un bajo, se vuelve uno de los más reconocibles del siglo."},
    {"anio": 2004, "titulo": "Nace el festival Altavoz en Medellín",
     "descripcion": "Plataforma pública para bandas de rock, metal, punk y otras músicas alternativas de la ciudad, que se consolida como referente de la escena local."},
    {"anio": 2016, "titulo": "Bob Dylan gana el Premio Nobel de Literatura",
     "descripcion": "La Academia Sueca reconoce sus letras, un hito para un artista surgido de la tradición folk y rock."},
    {"anio": 2021, "titulo": "Måneskin gana Eurovisión",
     "descripcion": "La banda italiana de rock se impone en el certamen y devuelve el género a la conversación del gran público."},
]

DECADAS_EXTRA = [
    {
        "slug": "2010s",
        "nombre": "Los 2010",
        "rango_anios": "2010 – 2019",
        "descripcion": (
            "El streaming cambia por completo cómo se escucha música y el "
            "rock comparte el protagonismo con el pop, el hip hop y la "
            "electrónica. Las bandas veteranas siguen llenando estadios, "
            "los festivales ganan peso y el indie y el rock alternativo "
            "se diversifican en decenas de propuestas."
        ),
        "subgeneros": ["Indie Rock", "Rock Alternativo", "Metal Moderno"],
    },
    {
        "slug": "2020s",
        "nombre": "Los 2020",
        "rango_anios": "2020 – hoy",
        "descripcion": (
            "La pandemia de 2020 detiene los conciertos en vivo y acelera "
            "el consumo en streaming y redes sociales. Con el regreso de "
            "los festivales, nuevas bandas alcanzan público global y las "
            "escenas locales, como la de Medellín, recuperan sus "
            "escenarios."
        ),
        "subgeneros": ["Rock Alternativo", "Indie Rock", "Revival"],
    },
]