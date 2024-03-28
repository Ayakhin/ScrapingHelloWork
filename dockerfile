FROM python:3.9-slim AS scrapy

RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev mariadb-client build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ] # Remplacez "app.py" par le point d'entrée de votre application
