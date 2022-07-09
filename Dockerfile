FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y

RUN apt install -y sudo

RUN apt install -y python3

RUN apt install -y python3-pip

RUN useradd -U -m django

RUN usermod -aG sudo django 

RUN usermod --shell /bin/bash django

RUN echo "django:django" | chpasswd

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

USER django

WORKDIR /home/django/BlueSkyRealty	

COPY ./requirements.txt /home/django/BlueSkyRealty/requirements.txt	

RUN pip install -r requirements.txt
