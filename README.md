# Problem: Active Shooter Response Time

- It can take 10-20 minutes for the authorities to arrive at an active shooter incident.

https://www.guard911.com/the-difference-between-active-shooter-notification-time-response-time/

# Solution

- Develop an AI model that can detect someone with a weapon and notify the authorities instantly.

# Project Outline

1. Collect/clean/store image data

2. Train/Test/Develop Model

3. Deploy app where you can upload images

# Tools:

- Python

- AWS S3

- Airflow

- Docker

- Kubernetes

- VGG Image Annotator

# Project Steps

## 1. Set up Notebook

```
% python -m venv weapon-detection                             # create virtual environment
% source weapon-detection/bin/activate                        # activate virtual environment
% python -m pip install --upgrade pip                         # upgrade pip version
% pip install ipykernel                                       # install ipykernel
% python -m ipykernel install --user --name=weapon-detection  # add virtual environment as a kernel
```

## 2. Collect and Store Image Data

- Pull image urls from Google API

- Store URL's in S3

- Download URL's using the links from S3

- Store images in S3

## 3. Annotate images

- Annotate by hand all the Gun images stored in S3

## 4. Train Model with annotated images

## 5. Test Model

## 6. Deploy Data Collection/Storage to Airflow (running in a Docker container)

## 7. Deploy model as a Flask/React app to Docker and Kubernetes

