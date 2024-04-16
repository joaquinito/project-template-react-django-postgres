# React + Django + PostgreSQL template

This template contains:
* a backend (folder 'server') running with Django
* a frontend (folder 'client') using on the React library, started with Vite
* a PostgreSQL database hosted in a cloud service

The file package.json in 'client' contains the Javascript libraries necessary for the frontend and a custom build script that copies the built frontend to the 'frontend' app in Django.
The file requirements.txt contains the Python libraries necessary for the backend.

Dependencies installed for client: `axios`

Dependencies installed for server: `dj-database-url`, `Django`, `django-cors-headers`, `djangorestframework`, `psycopg2`, `python-dotenv`

## Commands

In the client:

* `npm run dev`: run the client in development mode
* `npm run build`: build the client for production - it will copy the files to the 'frontend' app in Django

In the server:

* `python manage.py runserver`: run the server in development mode


## Requirements

A .env file is required in the root folder, containing the following variables:
* `DJANGO_SECRET_KEY`: the secret key for Django
* `DJANGO_DEBUG`: `True` or `False` depending on whether you want to run Django in debug mode
* `POSTGRESQL_DB_URL`: the URL for the PostgreSQL database