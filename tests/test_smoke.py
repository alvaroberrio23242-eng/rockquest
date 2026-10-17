import os

import pytest

os.environ.setdefault("SECRET_KEY", "clave-solo-para-pruebas")

from app import create_app  # noqa: E402

PAGES = [
    "/", "/historia", "/linea-del-tiempo", "/decadas", "/subgeneros",
    "/bandas", "/artistas", "/grammys", "/records", "/trivia", "/ruta-rockera",
]
SECTIONS = [
    "inicio", "ruta-rockera", "historia", "linea-del-tiempo", "decadas",
    "subgeneros", "bandas", "artistas", "grammys", "records", "trivia",
]
STATIC = [
    "css/onepage.css", "css/site.css", "css/ruta-rockera.css",
    "js/nav.js", "js/ruta-rockera.js",
    "vendor/markercluster/leaflet.markercluster.js",
    "vendor/markercluster/MarkerCluster.css",
]


@pytest.fixture(scope="module")
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


@pytest.mark.parametrize("path", PAGES)
def test_page_returns_200(client, path):
    response = client.get(path)
    assert response.status_code == 200
    assert b"RockQuest" in response.data


def test_unknown_route_is_404(client):
    assert client.get("/no-existe").status_code == 404


@pytest.mark.parametrize("path", ["/", "/bandas"])
@pytest.mark.parametrize("orden", ["popularidad", "grammys", "ventas", "influencia", "invalido"])
def test_orden_param_never_breaks(client, path, orden):
    assert client.get(path, query_string={"orden": orden}).status_code == 200


@pytest.mark.parametrize("section", SECTIONS)
def test_onepage_has_every_section(client, section):
    html = client.get("/").get_data(as_text=True)
    assert 'id="' + section + '"' in html


def test_onepage_single_hero_counter_and_single_leaflet(client):
    html = client.get("/").get_data(as_text=True)
    assert html.count('id="hero-count"') == 1
    assert html.count("leaflet.js") == 1


@pytest.mark.parametrize("path", STATIC)
def test_static_assets_are_served(client, path):
    response = client.get("/static/" + path)
    assert response.status_code == 200
    response.close()


def test_background_video_is_served(client):
    response = client.get("/static/videos/rockquest-bg.mp4")
    assert response.status_code in (200, 206)
    response.close()


def test_api_ruta_rockera_shape(client):
    response = client.get("/api/ruta-rockera")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data["count"] == len(data["places"])
    assert data["count"] > 0


def test_api_places_have_name_type_and_unique_ids(client):
    places = client.get("/api/ruta-rockera").get_json()["places"]
    for place in places:
        assert place.get("name")
        assert place.get("type")
    ids = [p["id"] for p in places if p.get("id")]
    assert len(ids) == len(set(ids))