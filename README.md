<<<<<<< HEAD
# 🎸 RockQuest

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-DB-07405E?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/status-en%20desarrollo-yellow)

**RockQuest** es una aplicación web interactiva que recorre la historia del Rock: bandas, artistas, décadas, subgéneros, récords y premios Grammy, con una estética oscura "neón" y fondo de video en loop.

---

## 🌟 Características

- 🎬 **Fondo de video rotativo** con tarjetas de vidrio esmerilado (glassmorphism).
- 🕰️ **Línea de tiempo** de hitos del rock.
- 📼 **Décadas** — bandas agrupadas por su década principal, tomadas en vivo desde la base de datos.
- 🎼 **Subgéneros** — cruce automático entre subgénero y bandas cuyo género coincide.
- 🎸 **Bandas** con orden por popularidad, Grammys, ventas o influencia.
- 🎤 **Artistas** — perfiles individuales con biografía.
- 🏆 **Grammys** y **Récords** históricos del género.
- ❓ **Trivia** de rock.
- ✨ Efectos de hover (Hover.css) y parallax de fondo.

---

## 🛠️ Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python / Flask (Blueprints) |
| Base de datos | SQLite / SQLAlchemy |
| Frontend | HTML5, CSS3 (glassmorphism + neón), JavaScript (vanilla + jQuery para parallax) |
| Control de versiones | Git & GitHub |

---

## 📁 Estructura del proyecto

```
rockquest/
├── run.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── seed.py                # Carga bandas iniciales
    ├── seed_artistas.py       # Carga artistas iniciales
    ├── seed_grammys.py        # Carga premios Grammy iniciales
    ├── seed_records.py        # Carga récords iniciales
    ├── models/                # Banda, Artista, Grammy, Record + datos estáticos (décadas, subgéneros, trivia, línea de tiempo)
    ├── routes/main.py         # Todas las rutas de la app
    ├── services/utils.py      # Slugs de imagen + imágenes genéricas de reemplazo
    ├── static/
    │   ├── css/                # style.css, hover.css
    │   ├── js/                 # video-bg.js, jquery.parallax.js, main.js, trivia.js
    │   ├── videos/              # rock-1.mp4, rock-2.mp4, rock-3.mp4
    │   └── images/              # bandas/, artistas/, grammys/, records/ (ver nota abajo)
    └── templates/
```

---

## 🚀 Cómo ejecutar la aplicación localmente

```bash
# 1. Clonar el repositorio
git clone <URL-de-tu-repo>
cd rockquest

# 2. Crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Cargar los datos iniciales (bandas, artistas, grammys, récords)
python -m app.seed
python -m app.seed_artistas
python -m app.seed_grammys
python -m app.seed_records

# 5. Ejecutar la aplicación
python run.py
```

La app queda disponible en `http://127.0.0.1:5000`.

> Los scripts de `seed_*.py` **insertan** filas nuevas — no actualizan las existentes. Si ya corriste una versión anterior, borrá `instance/rockquest.db` antes de repetir el paso 4 para evitar duplicados.

---

## 🖼️ Sobre las imágenes de bandas/artistas/grammys/récords

Estas cuatro carpetas (`static/images/bandas/`, `artistas/`, `grammys/`, `records/`) están vacías a propósito: las fotos reales de una banda o artista específico, y el arte de tapa de un álbum, tienen derechos de autor y no se pueden distribuir libremente en un repo público.

Por eso, `app/services/utils.py` incluye `imagen_generica()`, que asigna una foto decorativa de tema rock (guitarra, vinilo, escenario, micrófono) con licencia [Unsplash](https://unsplash.com/license) (uso comercial libre, sin atribución) en vez de una foto real. Si más adelante conseguís los derechos de una foto específica, podés:

1. Colocarla en `static/images/<categoria>/<slug>.jpg` (el slug exacto lo genera `slugify()` a partir del nombre — ver `imagen_url()` en `utils.py`).
2. Cambiar `imagen_generica(...)` por `imagen_url(...)` en el `seed_*.py` correspondiente.

---

## 🗺️ Roadmap

- [ ] Imágenes propias con licencia para bandas/artistas destacados
- [ ] Más bandas, artistas y décadas
- [ ] Panel de administración

---

## 📄 Licencia

Proyecto en desarrollo activo — licencia por definir.
=======
# 🎸 RockQuest

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-DB-07405E?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/status-en%20desarrollo-yellow)

**RockQuest** es una aplicación web interactiva diseñada para amantes del rock, turistas musicales y aficionados que desean explorar la historia del género de una forma inmersiva. A través de storytelling, trivia gamificada, contenido multimedia y experiencias interactivas, el usuario viaja por la evolución del rock desde sus orígenes hasta la actualidad, con una estética inspirada en escenarios de conciertos, luces LED, guitarras eléctricas y neones.

---

# 🌟 Características

- 🎬 **Fondo de video dinámico** con conciertos, escenarios, ciudades icónicas del rock y efectos de luces, acompañado de tarjetas con efecto **Glassmorphism**.

- 🎸 **Museo del Rock** con cientos de álbumes, guitarras, vestuarios, objetos históricos y curiosidades.

- 📜 **Historia del Rock** desde los años 50 hasta la actualidad.

- 🕰️ **Línea de tiempo interactiva** con filtros por década:
  - 1950s
  - 1960s
  - 1970s
  - 1980s
  - 1990s
  - 2000s
  - 2010+
  - Incluye imágenes, videos, audio y curiosidades.

- 🎤 **Biografías completas** de las bandas y artistas más importantes:
  - Queen
  - The Beatles
  - Led Zeppelin
  - Pink Floyd
  - AC/DC
  - Metallica
  - Nirvana
  - Guns N' Roses
  - The Rolling Stones
  - U2
  - Bon Jovi
  - Deep Purple
  - Iron Maiden
  - Black Sabbath
  - Foo Fighters
  - Red Hot Chili Peppers
  - Linkin Park
  - Muse
  - Arctic Monkeys
  - Green Day
  - y muchos más.

- 💿 **Los 100 álbumes más influyentes** del rock con:
  - Portada
  - Historia
  - Canciones
  - Premios
  - Datos curiosos

- 🎸 **Las guitarras más famosas de la historia**
  - Fender Stratocaster
  - Gibson Les Paul
  - Flying V
  - SG
  - Explorer
  - PRS
  - Jackson
  - Ibanez
  - Historia y artistas que las utilizaron.

- 🏆 **Récords del Rock**
  - Álbumes más vendidos
  - Giras más exitosas
  - Conciertos históricos
  - Récord Guinness
  - Bandas más premiadas

- 🌎 **Mapa Mundial del Rock**
  - Liverpool
  - Londres
  - Seattle
  - Los Ángeles
  - Nueva York
  - Nashville
  - Detroit
  - Berlín
  - Buenos Aires
  - Medellín
  - Tokio
  - Museos
  - Estudios
  - Bares históricos
  - Monumentos

- 🎵 **Spotify Player**
  - Classic Rock
  - Hard Rock
  - Progressive
  - Grunge
  - Punk
  - Alternative
  - Indie
  - Heavy Metal

- 🎮 **Trivia RockQuest**
  - Desafío diario
  - Sistema de experiencia
  - Logros
  - Insignias
  - Niveles
  - Recompensas

- 🏅 **Leaderboard mundial**

- 👤 **Registro de usuarios**

- 🎥 **Documentales recomendados**

- 📺 **Conciertos históricos**

- 🎼 **Historia de los instrumentos**
  - Guitarra
  - Bajo
  - Batería
  - Teclados
  - Sintetizadores

- 🎧 **Subgéneros del Rock**
  - Rock & Roll
  - Blues Rock
  - Psychedelic Rock
  - Progressive Rock
  - Glam Rock
  - Hard Rock
  - Punk Rock
  - New Wave
  - Heavy Metal
  - Thrash Metal
  - Death Metal
  - Black Metal
  - Nu Metal
  - Alternative Rock
  - Indie Rock
  - Grunge
  - Britpop
  - Garage Rock
  - Post Rock
  - Shoegaze
  - Emo
  - Pop Rock

- 🎫 **Festivales Legendarios**
  - Woodstock
  - Live Aid
  - Rock in Rio
  - Download Festival
  - Wacken Open Air
  - Hellfest
  - Lollapalooza
  - Glastonbury
  - Monsters of Rock

- 📻 **Emisoras de Rock del mundo**

- 🏛️ **Rock Hall of Fame**

- 📚 **Curiosidades y datos históricos**

- 🌐 Preparado para contenido multilingüe (ES / EN / FR / DE).

---

# 🛠️ Tecnologías

| Capa | Tecnología |
|------|------------|
| Backend | Python / Flask (Blueprints) |
| Base de datos | SQLite / SQLAlchemy |
| Frontend | HTML5, CSS3 (Glassmorphism + Neon + Dark Theme), JavaScript (Vanilla, Fetch API) |
| UI | Bootstrap 5, Font Awesome |
| Multimedia | Spotify API, YouTube Embed |
| Control de versiones | Git & GitHub |

---

# 📁 Estructura del proyecto

```text
rockquest/
├── run.py
├── init_db.py
├── requirements.txt
└── app/
    ├── __init__.py
    ├── models/
    │   ├── user.py
    │   ├── timeline_data.py
    │   ├── bands.py
    │   ├── albums.py
    │   ├── guitars.py
    │   ├── festivals.py
    │   ├── museums.py
    │   ├── records.py
    │   ├── genres.py
    │   └── visit_counter.py
    ├── routes/
    │   ├── main.py
    │   ├── auth.py
    │   ├── timeline.py
    │   ├── bands.py
    │   ├── albums.py
    │   ├── guitars.py
    │   ├── genres.py
    │   ├── festivals.py
    │   ├── museums.py
    │   ├── records.py
    │   └── leaderboard.py
    ├── services/
    │   ├── ia_service.py
    │   ├── spotify_service.py
    │   └── youtube_service.py
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   ├── js/
    │   │   ├── timeline.js
    │   │   ├── trivia.js
    │   │   ├── albums.js
    │   │   ├── bands.js
    │   │   ├── guitars.js
    │   │   ├── map.js
    │   │   └── player.js
    │   ├── videos/
    │   │   ├── concert1.mp4
    │   │   ├── concert2.mp4
    │   │   ├── stage.mp4
    │   │   └── stadium.mp4
    │   ├── img/
    │   └── audio/
    └── templates/
        ├── index.html
        ├── trivia.html
        ├── museum.html
        ├── albums.html
        ├── bands.html
        ├── guitars.html
        ├── timeline.html
        ├── map.html
        └── leaderboard.html
```

---

# 🚀 Cómo ejecutar la aplicación localmente

## Requisitos

Tener instalado **Python 3.8+**

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/alvaroberrio23242-eng/rockquest.git

cd rockquest

# Crear entorno virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python run.py
```

La aplicación estará disponible en:

```
http://127.0.0.1:5000
```

---

# 🎬 Recursos Multimedia

Los videos ubicados en:

```
app/static/videos/
```

contienen conciertos, festivales, escenarios y ciudades emblemáticas del rock.

Para optimizar el rendimiento en dispositivos móviles se recomienda comprimirlos:

```bash
ffmpeg -i concierto.mp4 -vf scale=1280:-1 -crf 28 app/static/videos/concert1.mp4
```

---

# 🗺️ Roadmap

- [ ] Integración con Spotify API
- [ ] Integración con YouTube API
- [ ] Modo VR para explorar museos del rock
- [ ] Mapa interactivo mundial del rock
- [ ] Biblioteca con más de 2.000 álbumes
- [ ] Más de 500 biografías de artistas
- [ ] Inteligencia Artificial para recomendar música según gustos del usuario
- [ ] Logros desbloqueables
- [ ] Sistema de coleccionables digitales
- [ ] Editor de contenido para administradores
- [ ] Aplicación Android e iOS
- [ ] Modo offline
- [ ] Traducción completa (Español, Inglés, Francés, Alemán, Portugués)
- [ ] Comunidad con perfiles, comentarios y rankings globales

---

# 🎯 Objetivo del proyecto

RockQuest busca convertirse en una de las plataformas educativas e interactivas más completas sobre la historia del rock, combinando videojuegos, cultura musical, inteligencia artificial y contenido multimedia en una experiencia moderna que permita descubrir más de 70 años de evolución del género.
>>>>>>> 2583249a2959b3a8344a59846b66f260d3fb6b26
