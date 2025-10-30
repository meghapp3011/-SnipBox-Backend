# -SnipBox-Backend

SnipBox is a simple note-saving backend application built with Django REST Framework.  
It allows users to save short text snippets, organize them with tags, and manage their data securely using JWT authentication.

# Features

- User authentication using **JWT 
- CRUD operations for snippets
- Tag management 
- Overview endpoint showing total snippets and list
- Each user can only access their own snippets

# Installation Guide

  ## clone the repository

 - git clone https://github.com/meghapp3011/-SnipBox-Backend.git
  
  ## Env setup
 
 - python -m venv venv  ( for creating virtual env)
 
 - source venv/bin/activate (activate virtual env)

  ## Installing dependencies

 - pip install -r requirements.txt

  ## Database migration

 - python manage.py makemigrations

 - python manage.py migrate

 - python manage.py createsuperuser ( create a super user)

 ## Run application

 - python manage.py runserver ( finally run the server)

