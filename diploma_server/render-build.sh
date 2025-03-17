#!/bin/bash

pip install -r requirements.txt

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('maratadmin', 'marat.chinerug@gmail.com', 'F1r3E1e2myD4D!') if not User.objects.filter(username='maratadmin').exists() else None" | python manage.py shell