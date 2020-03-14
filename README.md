# Django-Crowd_fundingding

Django-Crowd_fundingding is a Crowd clone made for fun.

## Prerequisities
* Python 3
* Django 1.10
* pip

## Installation Instructions
1. Clone the repository
2. Navigate into the django-Crowd_fundingding directory
3. Rename the file crowd_funding/settings_secret.py.template to crowd/settings.py and fill the DJANGO_KEY variable
4. pip install -r requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver

You can access the home page by visiting http://localhost:8000
