FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt ./app
COPY . . 

RUN apt-get update \
    && apt-get install -yyq netcat

RUN pip uninstall django
RUN pip install -r requirements.txt

EXPOSE 8000


COPY entrypoint.sh .
ENTRYPOINT ["sh", "entrypoint.sh"]