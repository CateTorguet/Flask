FROM python:3.10
MAINTAINER CateTorguet <pablo.castillot@edu.uah.es>

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
COPY ./app /app

CMD python main.py
RUN pip install -r requirements.txt
EXPOSE 5000
