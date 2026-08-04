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