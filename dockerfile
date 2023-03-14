FROM python:3.8

RUN apt-get update

WORKDIR /horta

COPY ./ .



FROM python:3.9

RUN apt-get update

WORKDIR /tcc

COPY ./ .

RUN pip install requests
RUN pip install paho-mqtt
RUN pip install schedule

CMD [ "python", "./tcc.py" ]
