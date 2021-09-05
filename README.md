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

- SQL

- Docker

- Kubernetes

- VGG Image Annotator

- AWS

# Project Steps

## 1. Set up Notebook

```
% python -m venv weapon-detection                 # create virtual environment
% source weapon-detection/bin/activate            # activate virtual environment
% python -m pip install --upgrade pip             # upgrade pip version
% pip install ipykernel                           # install ipykernel
% python -m ipykernel install --user --name=tfwd  # add virtual environment as a kernel
```

## 2. Collect and Store Image Data


