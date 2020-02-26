from flask import current_app as app
from .models import db, SmogMetric


@app.route('/', methods=['GET'])
def create_user():
    return 'main page'


@app.route('/api/dt/<pm10>/<pm25>/<temperature>/<humidity>/<time>', methods=['GET'])
def dust_and_temperature(pm10, pm25, temperature, humidity, time):
    return f'dust and temperature - {pm10} for {time}'


@app.route('/api/t/<temperature>/<humidity>', methods=['GET'])
def temperature(temperature, humidity):
    return f'temp: {float(temperature)}'
