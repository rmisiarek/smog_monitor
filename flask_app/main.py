from flask import Flask
app = Flask(__name__)


@app.route('/api/dt/<pm10>/<pm25>/<temperature>/<humidity>/<time>')
def dust_and_temperature(pm10, pm25, temperature, humidity, time):

    return f'dust and temperature - {pm10} for {time}'


@app.route("/api/t/<temperature>/<humidity>")
def temperature(temperature, humidity):
    return f"temp: {float(temperature)}"
