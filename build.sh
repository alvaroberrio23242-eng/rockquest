#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python -m app.seed
python -m app.seed_artistas
