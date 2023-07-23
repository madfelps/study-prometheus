import json
import time

import requests
from prometheus_client import Gauge, start_http_server

url_numero_pessoas = "http://api.open-notify.org/astros.json"
url_local_ISS = "http://api.open-notify.org/iss-now.json"


def get_local_ISS():
    try:
        response = requests.get(url_local_ISS)
        data = response.json()
        return data['iss_position']
    except Exception as e:
        print("We got some problems to access URL")
        raise e


def get_astronauts_number():
    try:
        response = requests.get(url_numero_pessoas)
        data = response.json()
        return data['number']
    except Exception as e:
        print("We got some problems to access URL")
        raise e


def update_metrics():
    try:
        number_astronauts = Gauge(
            'number_astronauts', 'Number of astronauts on space')
        longitude_ISS = Gauge('longitude_ISS', 'Longitude of ISS')
        latitude_ISS = Gauge('latitude_ISS', 'Latitude of ISS')
        while True:
            number_astronauts.set(get_astronauts_number())
            longitude_ISS.set(get_local_ISS()['longitude'])
            latitude_ISS.set(get_local_ISS()['latitude'])

            time.sleep(10)
            print(
                f'The number of astronauts on space is {get_astronauts_number()}')
            print(
                f'The longitude of ISS is {get_local_ISS()["longitude"]}')
            print(
                f'The latitude of ISS is {get_local_ISS()["latitude"]}'
            )
    except Exception as e:
        print("We got some problems to update metrics")
        raise e


def init_exporter():
    try:
        start_http_server(8899)
        return True
    except Exception as e:
        print("We got some problems to start http server")
        raise e


def main():
    try:
        init_exporter()
        print("HTTP Server initiliazed")
        update_metrics()
    except Exception as e:
        print("We got some problems to update metrics in exporter")
        exit(1)


if __name__ == "__main__":
    main()
    exit(0)
