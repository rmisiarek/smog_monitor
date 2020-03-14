import time

import requests
from requests.exceptions import ConnectionError
import Adafruit_DHT

from sds011 import sds011


FLASK_URL = "http://192.168.0.129:5555"
SDS011_ENDPOINT = FLASK_URL + "/api/{pm10}/{pm25}/{temperature}/{humidity}"
HDT22_ENDPOINT = FLASK_URL + "/api/t/{temperature}/{humidity}"

sensor_dht22_pin = 4
sensor_dht22 = Adafruit_DHT.DHT22
sensor_sds011 = sds011.SDS011("/dev/ttyUSB0")
sensor_sds011.set_duty_cycle(1)


def get_temperature_and_humidity():
    humidity, temperature = Adafruit_DHT.read(sensor_dht22, sensor_dht22_pin)

    return {
        "temperature": round(temperature, 1) if temperature else 0,
        "humidity": round(humidity, 1) if humidity else 0
    }


def send_request(r):
    try:
        requests.get(r)
    except ConnectionError:
        pass


while True:
    try:
        r = sensor_sds011.sender.read()
        if sensor_sds011.sender.is_valid_active_response(r):
            sds011_data = sensor_sds011.extract_pm_values(r)
            hdt22_data = get_temperature_and_humidity()

            if sds011_data and hdt22_data:
                sds011_data.update(
                    {
                        "temperature_c": hdt22_data["temperature"],
                        "humidity": hdt22_data["humidity"]
                    }
                )

            r = SDS011_ENDPOINT.format(
                pm10=sds011_data["pm10"],
                pm25=sds011_data["pm25"],
                temperature=hdt22_data["temperature"],
                humidity=hdt22_data["humidity"]
            )
            send_request(r)

        # th_data = get_temperature_and_humidity()
        # r = HDT22_ENDPOINT.format(
        #     temperature=th_data["temperature"], humidity=th_data["humidity"]
        # )
        # send_request(r)

        time.sleep(1)

    except KeyboardInterrupt:
        exit("\nBye!")
