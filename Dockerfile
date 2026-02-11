FROM python:3.14.2-alpine3.23

WORKDIR /code

COPY ./src/ ./src
COPY ./videos.json ./videos.json
COPY ./requirements.txt ./requirements.txt


RUN pip install -r requirements.txt

WORKDIR /code/src

CMD python -m db.init_db; python -m core.bot.main; sleep infinity