# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

ADD . /labyrinth_solver
WORKDIR /labyrinth_solver

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip & \
pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]