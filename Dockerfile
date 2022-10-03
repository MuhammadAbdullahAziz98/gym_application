FROM python:3.8.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
# Set work directory

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt

EXPOSE 8000 

# Remove "pipenv run", add the bind argument
# (No need to repeat `command:` in `docker-compose.yml`)
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  
COPY . $DockerHOME  


CMD python manage.py runserver 0.0.0.0:8000