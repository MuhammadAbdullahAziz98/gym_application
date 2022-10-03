# Gym Application Service
A python django based rest API for athletes to manage their daily calories at the gym. Uses python 3.8.9

## Install dependencies / packages:

```
pipenv install
```

## run virtual environment:
```
pip install pipenv

pipenv shell
```

## run the app:
```
python manage.py runserver
```

check example .env file (.env.example) for setting up database (postgreSQL used)

## Run migrations:

```
python manage.py makemigrations

python manage.py migrate
```

## for test coverage use:

Test coverage is 70% above in most cases.

```
coverage run manage.py test

coverage report
```

## To make super user / admin user:
```
python manage.py createsuperuser
```

## access admin panel via:
http://localhost:8000/admin/

## Register using:

localhost:8000/core/register/

#### Example request:
```

{
    "email": "",
    "password": "",
    "password2": "",
    "first_name": "",
    "last_name": "",
    "username": ""
}
```

## Login Via:
http://localhost:8000/accounts/login

## Get JWT Token (to use with postman etc) Via:
http://localhost:8000/api/token/

## Swagger docs available at:
http://localhost:8000/swagger/

## Open API specifications:
http://localhost:8000/redoc/

# Example API call to get calories burnt per day (authentication implemented):
http://localhost:8000/athlete/calories-consumed?start_date=2022-09-29&end_date=2022-10-05

^ for using above API call you need to first add equipment (via POST call), then add exercise using that equipment (post API call), then perform exercise using following POSt API call:
http://localhost:8000/athlete/exercise/

#### Example request body:

```
{
  "exercise_date": "2022-10-03",
  "athlete": 1,
  "exercise": 1
}
```

## Run docker image using:

```
DOCKER_BUILDKIT=0  docker build . -t docker-gym-app

docker run docker-gym-app
```

(SQL connection is missing in with the docker image)
