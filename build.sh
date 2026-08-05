#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
# NOTA: seed.py y seed_artistas.py NO se corren aca a proposito.
# Correrlos en cada deploy duplicaria bandas y artistas.
# Se corren a mano, UNA sola vez, desde el Shell de Render:
#   python -m app.seed
#   python -m app.seed_artistas
