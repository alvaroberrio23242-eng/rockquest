"""
Ruta Rockera — Base maestra de lugares.

Fuente editorial:
- Investigación web de la escena rock de Medellín y Valle de Aburrá.
- Fuentes institucionales, medios especializados y establecimientos.
- Coordenadas preparadas para representación cartográfica.

IMPORTANTE:
Este archivo contiene datos editoriales. No contiene lógica del mapa.
El frontend debe consumir esta estructura sin duplicar los datos.

Estados:
    ACTIVE       Lugar actualmente activo.
    HISTORICAL   Lugar de importancia histórica.
    CULTURAL     Escenario / museo / festival / infraestructura cultural.
    VERIFY       Candidato pendiente de verificación adicional.

Evidence:
    VERIFIED_PRIMARY
    VERIFIED_SECONDARY
    HISTORICAL_DOCUMENTED
    NOT_VERIFIED

Tipos:
    ROCK_BAR
    METAL_BAR
    LIVE_MUSIC_BAR
    CULTURAL_VENUE
    MUSEUM
    FESTIVAL
    HISTORICAL_SITE
"""

from copy import deepcopy


RUTA_ROCKERA = [
    # ============================================================
    # ESCENARIOS CULTURALES
    # ============================================================

    {
        "id": "teatro-carlos-vieco",
        "name": "Teatro al Aire Libre Carlos Vieco Ortiz",
        "type": "CULTURAL_VENUE",
        "status": "CULTURAL",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "Cerro Nutibara",
        "address": "Cerro Nutibara, Medellín, Antioquia",
        "coordinates": {
            "lat": 6.2390,
            "lng": -75.5790,
        },
        "music_styles": [
            "Rock",
            "Metal",
            "Punk",
            "Core",
            "Música alternativa",
        ],
        "description": (
            "Escenario cultural emblemático de Medellín vinculado durante "
            "décadas con conciertos, procesos de música alternativa y "
            "eventos como Ciudad Altavoz."
        ),
        "historical": True,
        "current_activity": True,
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": [
            {
                "name": "Alcaldía de Medellín",
                "url": (
                    "https://www.medellin.gov.co/es/sala-de-prensa/"
                    "noticias/ciudad-altavoz-reunira-a-70-bandas-en-el-"
                    "teatro-al-aire-libre-carlos-vieco-ortiz-ya-esta-la-"
                    "lista-de-las-agrupaciones-seleccionadas/"
                ),
                "type": "INSTITUTIONAL",
            },
            {
                "name": "Medellín.Travel",
                "url": (
                    "https://www.medellin.travel/caleventos/"
                    "ciudad-altavoz-2026-641/"
                ),
                "type": "INSTITUTIONAL",
            },
        ],
        "tags": [
            "Carlos Vieco",
            "Altavoz",
            "rock paisa",
            "escenario",
            "Medellín",
        ],
    },

    {
        "id": "murock-casa-musica",
        "name": "MUROCK — Museo Rock Medellín / Casa de la Música",
        "type": "MUSEUM",
        "status": "CULTURAL",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "Parque de los Deseos",
        "address": "Casa de la Música, Parque de los Deseos, Medellín",
        "coordinates": {
            "lat": 6.2630,
            "lng": -75.5660,
        },
        "music_styles": [
            "Rock",
            "Metal",
            "Punk",
            "Rock colombiano",
        ],
        "description": (
            "Espacio dedicado a preservar y divulgar la historia del rock "
            "de Medellín y Antioquia, integrado a la Casa de la Música."
        ),
        "historical": True,
        "current_activity": True,
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": [
            {
                "name": "Fundación EPM",
                "url": (
                    "https://www.grupo-epm.com/fundacion-grupo-epm/"
                    "noticias/boletines-de-prensa-2025/"
                    "Medellin-ya-tiene-su-Museo-del-Rock--MUROCK-abre-"
                    "sus-puertas-con-el-respaldo-de-la-Fundacion-EPM--/"
                ),
                "type": "INSTITUTIONAL",
            },
        ],
        "tags": [
            "MUROCK",
            "museo",
            "historia",
            "rock paisa",
            "Casa de la Música",
        ],
    },

    # ============================================================
    # BARES Y ESTABLECIMIENTOS ACTUALES
    # ============================================================

    {
        "id": "la-cupula-rock-bar",
        "name": "La Cúpula Rock Bar",
        "type": "ROCK_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "El Poblado",
        "address": "Cra. 43A #10-38, El Poblado, Medellín",
        "coordinates": {
            "lat": 6.2090,
            "lng": -75.5680,
        },
        "music_styles": [
            "Rock",
            "Rock clásico",
            "Rock 80s",
            "Rock 90s",
            "Rock 2000s",
        ],
        "description": (
            "Bar especializado en rock con programación de música en vivo "
            "y repertorio asociado principalmente al rock de las décadas "
            "de 1980, 1990 y 2000."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Business listing",
                "url": "",
                "type": "CURRENT_BUSINESS",
            },
            {
                "name": "Tripadvisor",
                "url": (
                    "https://www.tripadvisor.es/Restaurant_Review-"
                    "g297478-d33321151-Reviews-La_Cupula_Rock_Bar-"
                    "Medellin_Antioquia_Department.html"
                ),
                "type": "SECONDARY",
            },
        ],
        "tags": [
            "rock bar",
            "música en vivo",
            "El Poblado",
        ],
    },

    {
        "id": "valhala-rock-bar",
        "name": "Valhala Rock Bar",
        "type": "ROCK_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "Belén",
        "address": "Cra. 81 #32-124 Local 135, Medellín",
        "coordinates": {
            "lat": 6.2350,
            "lng": -75.6020,
        },
        "music_styles": [
            "Rock",
            "Rock & Roll",
        ],
        "description": (
            "Rock bar de Belén asociado históricamente con la escena "
            "rockera de Nueva Villa de Aburrá."
        ),
        "historical": True,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Cartel Rock",
                "url": "https://cartelrock.com/comercio/valhala-rock-bar",
                "type": "SPECIALIZED_MEDIA",
            },
        ],
        "tags": [
            "rock bar",
            "rock & roll",
            "Belén",
            "Nueva Villa de Aburrá",
        ],
    },

    {
        "id": "retro-rock-metal-club",
        "name": "Retro Rock & Metal Club",
        "type": "METAL_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "La Candelaria",
        "address": "Cra. 43 #46-10, Medellín",
        "coordinates": {
            "lat": 6.2500,
            "lng": -75.5660,
        },
        "music_styles": [
            "Rock",
            "Hard Rock",
            "Metal",
            "Gothic",
            "Post-Punk",
        ],
        "description": (
            "Establecimiento orientado a rock y metal, con identidad "
            "asociada también a sonidos góticos, post-punk y rock clásico."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Business listing",
                "url": "",
                "type": "CURRENT_BUSINESS",
            },
            {
                "name": "Restaurant Guru",
                "url": (
                    "https://es.restaurantguru.com/"
                    "Retro-Rock-and-Metal-Club-Medellin"
                ),
                "type": "SECONDARY",
            },
        ],
        "tags": [
            "metal",
            "hard rock",
            "gothic",
            "post-punk",
            "Centro",
        ],
    },

    {
        "id": "dopamina-rock-bar-laureles",
        "name": "Dopamina Rock Bar Laureles",
        "type": "ROCK_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "Laureles - Estadio",
        "address": "Cl. 44 #80-31, Medellín",
        "coordinates": {
            "lat": 6.2450,
            "lng": -75.6010,
        },
        "music_styles": [
            "Rock",
            "Rock en vivo",
        ],
        "description": (
            "Bar de Laureles con programación asociada al rock y "
            "presentaciones de música en vivo."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Current business listing",
                "url": "",
                "type": "CURRENT_BUSINESS",
            },
        ],
        "tags": [
            "rock bar",
            "Laureles",
            "música en vivo",
        ],
    },

    {
        "id": "canterbury-cafe-medellin",
        "name": "Canterbury Café Medellín",
        "type": "LIVE_MUSIC_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "La Candelaria / Bomboná",
        "address": "Cl. 47 #42-38 Local 103, Medellín",
        "coordinates": {
            "lat": 6.2480,
            "lng": -75.5630,
        },
        "music_styles": [
            "Rock",
            "Música en vivo",
        ],
        "description": (
            "Café y bar musical con programación de música en vivo, "
            "incluyendo rock."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": [
            {
                "name": "Canterbury Café",
                "url": "https://canterburycafe.com.co/medellin",
                "type": "OFFICIAL",
            },
        ],
        "tags": [
            "rock",
            "música en vivo",
            "Bomboná",
            "Centro",
        ],
    },

    {
        "id": "bantu-bar",
        "name": "Bantú Bar",
        "type": "ROCK_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "La Candelaria / El Chagualo",
        "address": "Cl. 65 #55A-35, Medellín",
        "coordinates": {
            "lat": 6.2630,
            "lng": -75.5670,
        },
        "music_styles": [
            "Rock",
            "Rock & Roll",
        ],
        "description": (
            "Bar identificado dentro del circuito local de rock y "
            "rock & roll de Medellín."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Cartel Rock",
                "url": "https://cartelrock.com/comercio/bantu-bar",
                "type": "SPECIALIZED_MEDIA",
            },
        ],
        "tags": [
            "rock & roll",
            "rock bar",
            "El Chagualo",
        ],
    },

    {
        "id": "trilogia-bar",
        "name": "Trilogía Bar",
        "type": "LIVE_MUSIC_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "El Poblado",
        "address": "Cra. 43G #24-08, Medellín",
        "coordinates": {
            "lat": 6.2170,
            "lng": -75.5740,
        },
        "music_styles": [
            "Rock",
            "Salsa",
            "Tango",
            "Balada",
        ],
        "description": (
            "Bar de música en vivo con una programación diversa. "
            "El rock forma parte de su identidad musical, pero no es "
            "un establecimiento exclusivamente rockero."
        ),
        "historical": True,
        "current_activity": True,
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": [
            {
                "name": "Trilogía Bar",
                "url": "https://www.trilogiabar.com/",
                "type": "OFFICIAL",
            },
        ],
        "tags": [
            "música en vivo",
            "rock",
            "Poblado",
            "bar histórico",
        ],
    },

    {
        "id": "rock-symphony",
        "name": "Rock Symphony",
        "type": "ROCK_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "La Candelaria",
        "address": "Cl. 47 #42-76, Medellín",
        "coordinates": {
            "lat": 6.2480,
            "lng": -75.5650,
        },
        "music_styles": [
            "Rock",
            "Rock en vivo",
        ],
        "description": (
            "Establecimiento del circuito contemporáneo de bares "
            "rockeros de Medellín."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Current business listing",
                "url": "",
                "type": "CURRENT_BUSINESS",
            },
        ],
        "tags": [
            "rock bar",
            "Centro",
            "música",
        ],
    },

    {
        "id": "la-jaus-pub-rock",
        "name": "La Jaus Pub Rock",
        "type": "ROCK_BAR",
        "status": "ACTIVE",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "La Candelaria",
        "address": "Pasaje Cervantes, Cra. 42A #48-46, Medellín",
        "coordinates": {
            "lat": 6.2490,
            "lng": -75.5680,
        },
        "music_styles": [
            "Rock",
        ],
        "description": (
            "Pub identificado actualmente como establecimiento asociado "
            "al circuito rock de La Candelaria."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Current business listing",
                "url": "",
                "type": "CURRENT_BUSINESS",
            },
        ],
        "tags": [
            "rock pub",
            "Centro",
            "La Candelaria",
        ],
    },

    # ============================================================
    # VALLE DE ABURRÁ
    # ============================================================

    {
        "id": "balrog-metal-bar-itagui",
        "name": "BALROG Metal Bar",
        "type": "METAL_BAR",
        "status": "ACTIVE",
        "city": "Itagüí",
        "municipality": "Itagüí",
        "neighborhood": "Germania",
        "address": "Cl. 43 #49-18, Itagüí, Antioquia",
        "coordinates": {
            "lat": 6.1710,
            "lng": -75.6110,
        },
        "music_styles": [
            "Metal",
            "Rock",
        ],
        "description": (
            "Bar especializado en metal ubicado en Itagüí. "
            "Amplía la Ruta Rockera más allá de Medellín hacia "
            "el Valle de Aburrá."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": [
            {
                "name": "Current business listing",
                "url": "",
                "type": "CURRENT_BUSINESS",
            },
        ],
        "tags": [
            "metal",
            "metal bar",
            "Itagüí",
            "Valle de Aburrá",
        ],
    },

    {
        "id": "estacion-central-pub-envigado",
        "name": "Estación Central Pub",
        "type": "LIVE_MUSIC_BAR",
        "status": "VERIFY",
        "city": "Envigado",
        "municipality": "Envigado",
        "neighborhood": "Zona 9",
        "address": "Cra. 43 #31 Sur-32, Envigado",
        "coordinates": {
            "lat": 6.1700,
            "lng": -75.5850,
        },
        "music_styles": [
            "Rock",
            "Música en vivo",
        ],
        "description": (
            "Establecimiento del Valle de Aburrá identificado en "
            "la investigación como candidato del circuito musical. "
            "Su relación específica con el rock requiere verificación "
            "editorial adicional antes de marcarlo como confirmado."
        ),
        "historical": False,
        "current_activity": True,
        "evidence_status": "NOT_VERIFIED",
        "sources": [
            {
                "name": "Current business listing",
                "url": "",
                "type": "CURRENT_BUSINESS",
            },
        ],
        "tags": [
            "Envigado",
            "Valle de Aburrá",
            "candidato",
        ],
    },

    # ============================================================
    # SITIOS HISTÓRICOS
    # ============================================================

    {
        "id": "festival-ancon-la-estrella",
        "name": "Festival de Ancón — Sitio histórico",
        "type": "HISTORICAL_SITE",
        "status": "HISTORICAL",
        "city": "La Estrella",
        "municipality": "La Estrella",
        "neighborhood": "Ancón",
        "address": "Sector Ancón, La Estrella, Antioquia",
        "coordinates": {
            "lat": 6.1550,
            "lng": -75.6450,
        },
        "music_styles": [
            "Rock",
            "Rock colombiano",
            "Contracultura",
        ],
        "description": (
            "Lugar histórico asociado al Festival de Ancón de 1971, "
            "uno de los acontecimientos fundamentales de la historia "
            "del rock colombiano y paisa."
        ),
        "historical": True,
        "current_activity": False,
        "evidence_status": "HISTORICAL_DOCUMENTED",
        "sources": [
            {
                "name": "Alcaldía de La Estrella",
                "url": (
                    "https://2024.laestrella.gov.co/sitio/ver_noticia/"
                    "festivalancon"
                ),
                "type": "INSTITUTIONAL",
            },
        ],
        "tags": [
            "Ancón",
            "1971",
            "historia",
            "rock colombiano",
            "La Estrella",
        ],
    },

    {
        "id": "plaza-toros-la-macarena",
        "name": "Plaza de Toros La Macarena — Hito rockero",
        "type": "HISTORICAL_SITE",
        "status": "HISTORICAL",
        "city": "Medellín",
        "municipality": "Medellín",
        "neighborhood": "Laureles-Estadio",
        "address": "Plaza de Toros La Macarena, Medellín",
        "coordinates": {
            "lat": 6.2460,
            "lng": -75.5890,
        },
        "music_styles": [
            "Rock",
            "Heavy Metal",
        ],
        "description": (
            "Escenario que forma parte de la memoria histórica del "
            "rock de Medellín por conciertos documentados durante "
            "la década de 1980."
        ),
        "historical": True,
        "current_activity": False,
        "evidence_status": "HISTORICAL_DOCUMENTED",
        "sources": [
            {
                "name": "MUROCK / documentación histórica",
                "url": "",
                "type": "HISTORICAL",
            },
        ],
        "tags": [
            "historia",
            "La Macarena",
            "Metal Medallo",
            "rock paisa",
        ],
    },
]


# ================================================================
# ÍNDICES
# ================================================================

RUTA_ROCKERA_BY_ID = {
    place["id"]: place
    for place in RUTA_ROCKERA
}


def get_all_places():
    """Devuelve una copia de todos los lugares."""
    return deepcopy(RUTA_ROCKERA)


def get_active_places():
    """Devuelve únicamente establecimientos/espacios actualmente activos."""
    return deepcopy([
        place
        for place in RUTA_ROCKERA
        if place["status"] == "ACTIVE"
        or place.get("current_activity") is True
    ])


def get_historical_places():
    """Devuelve los lugares con valor histórico."""
    return deepcopy([
        place
        for place in RUTA_ROCKERA
        if place["status"] == "HISTORICAL"
        or place.get("historical") is True
    ])


def get_cultural_places():
    """Devuelve museos, escenarios y espacios culturales."""
    return deepcopy([
        place
        for place in RUTA_ROCKERA
        if place["status"] == "CULTURAL"
    ])


def get_place(place_id):
    """Busca un lugar por ID."""
    place = RUTA_ROCKERA_BY_ID.get(place_id)

    if place is None:
        return None

    return deepcopy(place)


def get_places_by_type(place_type):
    """Filtra por tipo."""
    return deepcopy([
        place
        for place in RUTA_ROCKERA
        if place["type"] == place_type
    ])


def get_places_by_city(city):
    """Filtra por ciudad/municipio."""
    normalized = city.strip().lower()

    return deepcopy([
        place
        for place in RUTA_ROCKERA
        if place["city"].lower() == normalized
        or place["municipality"].lower() == normalized
    ])


def get_places_by_style(style):
    """Filtra por género o estilo musical."""
    normalized = style.strip().lower()

    return deepcopy([
        place
        for place in RUTA_ROCKERA
        if any(
            normalized == item.lower()
            for item in place.get("music_styles", [])
        )
    ])


def get_verified_places():
    """Devuelve lugares con evidencia confirmada."""
    verified = {
        "VERIFIED_PRIMARY",
        "VERIFIED_SECONDARY",
        "HISTORICAL_DOCUMENTED",
    }

    return deepcopy([
        place
        for place in RUTA_ROCKERA
        if place["evidence_status"] in verified
    ])


def validate_ruta_rockera():
    """
    Valida integridad básica de la base maestra.

    Retorna:
        list[str]: lista de errores.
    """
    errors = []
    ids = set()

    required_fields = {
        "id",
        "name",
        "type",
        "status",
        "city",
        "municipality",
        "address",
        "coordinates",
        "music_styles",
        "description",
        "evidence_status",
        "sources",
    }

    valid_statuses = {
        "ACTIVE",
        "HISTORICAL",
        "CULTURAL",
        "VERIFY",
    }

    valid_evidence = {
        "VERIFIED_PRIMARY",
        "VERIFIED_SECONDARY",
        "HISTORICAL_DOCUMENTED",
        "NOT_VERIFIED",
    }

    for index, place in enumerate(RUTA_ROCKERA):
        prefix = f"places[{index}]"

        missing = required_fields - set(place.keys())

        if missing:
            errors.append(
                f"{prefix}: faltan campos {sorted(missing)}"
            )

        place_id = place.get("id")

        if not place_id:
            errors.append(f"{prefix}: ID vacío")
        elif place_id in ids:
            errors.append(f"{prefix}: ID duplicado: {place_id}")
        else:
            ids.add(place_id)

        if place.get("status") not in valid_statuses:
            errors.append(
                f"{prefix}: estado inválido: {place.get('status')}"
            )

        if place.get("evidence_status") not in valid_evidence:
            errors.append(
                f"{prefix}: evidencia inválida: "
                f"{place.get('evidence_status')}"
            )

        coordinates = place.get("coordinates", {})

        lat = coordinates.get("lat")
        lng = coordinates.get("lng")

        if not isinstance(lat, (int, float)):
            errors.append(f"{prefix}: latitud inválida")

        if not isinstance(lng, (int, float)):
            errors.append(f"{prefix}: longitud inválida")

        if isinstance(lat, (int, float)):
            if not -90 <= lat <= 90:
                errors.append(f"{prefix}: latitud fuera de rango")

        if isinstance(lng, (int, float)):
            if not -180 <= lng <= 180:
                errors.append(f"{prefix}: longitud fuera de rango")

        if not place.get("sources"):
            errors.append(f"{prefix}: sin fuentes")

    return errors


if __name__ == "__main__":
    errors = validate_ruta_rockera()

    print("=" * 60)
    print("RUTA ROCKERA — VALIDACIÓN")
    print("=" * 60)
    print(f"Total lugares: {len(RUTA_ROCKERA)}")

    if errors:
        print(f"Errores encontrados: {len(errors)}")

        for error in errors:
            print(f" - {error}")

        raise SystemExit(1)

    print("VALIDACIÓN OK")
    print()
    print("Por tipo:")

    types = sorted({
        place["type"]
        for place in RUTA_ROCKERA
    })

    for place_type in types:
        total = len(get_places_by_type(place_type))
        print(f" - {place_type}: {total}")

    print()
    print("Por estado:")

    statuses = sorted({
        place["status"]
        for place in RUTA_ROCKERA
    })

    for status in statuses:
        total = len([
            p for p in RUTA_ROCKERA
            if p["status"] == status
        ])

        print(f" - {status}: {total}")

    print()
    print("Por evidencia:")

    evidences = sorted({
        place["evidence_status"]
        for place in RUTA_ROCKERA
    })

    for evidence in evidences:
        total = len([
            p for p in RUTA_ROCKERA
            if p["evidence_status"] == evidence
        ])

        print(f" - {evidence}: {total}")
