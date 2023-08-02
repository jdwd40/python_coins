#!/bin/bash

# Activate the virtual environment
source env/bin/activate

# Install the required libraries
pip install Flask
pip install SQLAlchemy
pip install psycopg2-binary
pip install Flask-Migrate
pip install Flask-RESTful
pip install Flask-Bcrypt
pip install PyJWT

# Deactivate the virtual environment
deactivate
