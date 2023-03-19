#!/usr/bin/env bash
# exit on error
set -o errexit

CPATH=/opt/render/project/python/Python-3.10.10/include/python3.10/

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
