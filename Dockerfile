FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip install --upgrade pip
WORKDIR app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./insert_script.py/app

CMD python3 insert_script.py