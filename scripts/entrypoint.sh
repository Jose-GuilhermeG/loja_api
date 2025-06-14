#!/bin/bash
cd /usr/src/project/

./wait-for-it.sh mysql_container:3306 --timeout=30 --strict -- echo "MySQL está pronto!"

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000