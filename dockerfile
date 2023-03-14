FROM python:3.9

RUN apt-get update \
    && apt-get install -y unixodbc-dev build-essential libssl-dev libffi-dev python3-dev

WORKDIR /app


COPY . .

RUN pip install requests
RUN pip install paho-mqtt
RUN pip install schedule

CMD [ "python", "tcc.py" ]
