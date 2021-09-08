# start from python version 3.8
FROM python:3.8

# update package manager
RUN apt-get update -y 

# install dependencies for open-cv library
RUN apt-get install ffmpeg libsm6 libxext6  -y

# copy the requirements.txt to /app
COPY ./requirements.txt /app/requirements.txt

# upgrade pip
RUN pip install --upgrade pip

# set working directory to /app
WORKDIR /app

# install all the dependencies
RUN pip install -r requirements.txt

# install gunicorn
RUN pip install gunicorn

# copy all the project files to /app
COPY . /app

# make gunicorn_start.sh executable
RUN chmod +x gunicorn_start.sh

# start the gunicorn server
ENTRYPOINT ["./gunicorn_start.sh"]
