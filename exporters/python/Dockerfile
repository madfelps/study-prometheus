FROM python:3.8-slim 

LABEL maintainer Felipe Madureira <femadureira7@gmail.com>
LABEL description "Dockerfile para criar imagem de container do exporter em Python"

WORKDIR /app 
COPY . /app 
RUN pip3 install -r requirements.txt 

CMD python3 exporter.py 