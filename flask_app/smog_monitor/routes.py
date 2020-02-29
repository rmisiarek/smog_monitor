from flask import current_app as app
from flask import render_template, redirect, url_for
#from flask_socketio import emit

from .models import db, SmogMetric
from . import socketio


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/dt/<pm10>/<pm25>/<temperature>/<humidity>/<time>', methods=['GET'])
def dust_and_temperature(pm10, pm25, temperature, humidity, time):
    data = {
        'pm10': float(pm10),
        'pm25': float(pm25),
        'temperature': float(temperature),
        'humidity': float(humidity),
        'time': time
    }
    socketio.emit('dust_and_temperature', data)

    return redirect(url_for('index'))


@app.route('/api/t/<temperature>/<humidity>', methods=['GET'])
def temperature(temperature, humidity):
    data = {
        'temperature': float(temperature),
        'humidity': float(humidity)
    }
    socketio.emit('temperature', data)

    return redirect(url_for('index'))

@socketio.on('my event')
def handle_event(data):
    print(f'my event: {data}')
