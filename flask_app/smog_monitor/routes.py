from flask import current_app as app
from flask import render_template
from .models import db, SmogMetric
from . import socketio


@app.route('/', methods=['GET'])
def create_user():
    return render_template('index.html')


@app.route('/api/dt/<pm10>/<pm25>/<temperature>/<humidity>/<time>', methods=['GET'])
def dust_and_temperature(pm10, pm25, temperature, humidity, time):
    return f'dust and temperature - {pm10} for {time}'


@app.route('/api/t/<temperature>/<humidity>', methods=['GET'])
def temperature(temperature, humidity):
    return f'temp: {float(temperature)}'


@socketio.on('my event')
def handle_event(data):
    print(f'my event: {data}')
