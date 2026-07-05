#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username="varun").exists():
    User.objects.create_superuser(
        "varun",
        "varun.k.a.1005@gmal.com",
        "Varun51130"
    )
END