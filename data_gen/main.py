import time
import board
import adafruit_dht
from sds011 import sds011


sensor_dht22 = adafruit_dht.DHT22(board.D4)
sensor_sds011 = sds011.SDS011("/dev/ttyUSB0")
sensor_sds011.set_duty_cycle(1)


def get_temperature_and_humidity():
    try:
        temperature_c = sensor_dht22.temperature
        humidity = sensor_dht22.humidity
    except RuntimeError:
        temperature_c = 0.0
        humidity = 0.0
    else:
        return {
            "temperature_c": temperature_c,
            "humidity": humidity
        }


while True:
    try:
        r = sensor_sds011.sender.read()
        if sensor_sds011.sender.is_valid_active_response(r):
            sds011_data = sensor_sds011.extract_pm_values(r)
            hdt22_data = get_temperature_and_humidity()

            if sds011_data and hdt22_data:
                sds011_data.update(
                    {
                        "temperature_c": hdt22_data["temperature_c"],
                        "humidity": hdt22_data["humidity"]
                    }
                )

            print(sds011_data)

        th_data = get_temperature_and_humidity()
        print(th_data)

        time.sleep(1)

    except KeyboardInterrupt:
        exit("\nBye!")
