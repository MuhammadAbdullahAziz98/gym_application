# Gym Application Service
A python django based rest API for athletes to manage their daily calories at the gym. Uses python 3.8.9

## Install dependencies / packages:

pipenv install

## run pipenv:
pipenv shell

## run the app:
python manage.py runserver

check example .env file (.env.example) for setting up database (postgreSQL used)

# Run migrations:

python manage.py makemigrations

python manage.py migrate

## for test coverage use:

Test coverage is 70% above in most cases.

coverage run manage.py test

coverage report

# Register using:

localhost:8000/core/register/

####Example request:
{
    "email": "",
    "password": "",
    "password2": "",
    "first_name": "",
    "last_name": "",
    "username": ""
}

## Swagger docs available at:
http://localhost:8000/swagger/

## Run docker image using:

DOCKER_BUILDKIT=0  docker build . -t docker-gym-app

docker run docker-gym-app

(SQL connection is missing in with the docker image)
