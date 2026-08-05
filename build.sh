#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python -m app.seed
python -m app.seed_artistas
# seed_grammys.py y seed_records.py: agregar aca una vez revisados
