import re
from pathlib import Path

from app.models.ruta_rockera_data import get_verified_places

JS_PATH = Path(__file__).resolve().parent.parent / "app" / "static" / "js" / "ruta-rockera.js"
PLACES = get_verified_places()


def _js_keys(name):
    text = JS_PATH.read_text(encoding="utf-8")
    match = re.search(r"const " + name + r" = \{(.*?)\};", text, re.S)
    assert match is not None, "no encuentro " + name + " en ruta-rockera.js"
    return set(re.findall(r"([A-Z_]{3,}):", match.group(1)))


def test_every_place_type_is_supported_by_the_map():
    used = {p["type"] for p in PLACES}
    assert used <= _js_keys("TYPES")


def test_every_evidence_status_has_a_spanish_label():
    used = {p["evidence_status"] for p in PLACES}
    assert used <= _js_keys("EVIDENCE")


def test_every_place_has_numeric_coordinates():
    for place in PLACES:
        coords = place["coordinates"]
        assert isinstance(coords["lat"], (int, float))
        assert isinstance(coords["lng"], (int, float))