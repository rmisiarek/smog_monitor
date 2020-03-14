from flask import current_app as app
from flask import render_template, redirect, url_for
from sqlalchemy import desc
from flask_socketio import emit

from .models import SmogMetric
from . import socketio, db


FIRST_COLOR = '#606060FF'
SECOND_COLOR = '#D6ED17FF'
RECORDS_LIMIT = 60


def prepare_data():
    temperature_data = []
    humidity_data = []
    pm10_data = []
    pm25_data = []
    categories = []
    all_smog_data = SmogMetric.query.order_by(desc(SmogMetric.id)).limit(RECORDS_LIMIT).all()
    for data in reversed(all_smog_data):
        categories.append(data.created.strftime("%Y-%m-%d %H:%M:%S"))
        temperature_data.append(
            {
                "y": data.temperature,
                "color": SECOND_COLOR
            }
        )
        humidity_data.append(
            {
                "y": data.humidity,
                "color": FIRST_COLOR
            }
        )
        pm10_data.append(
            {
                "y": data.pm10,
                "color": FIRST_COLOR
            }
        )
        pm25_data.append(
            {
                "y": data.pm25,
                "color": SECOND_COLOR
            }
        )

    weather_data = {
        "temperature": temperature_data,
        "humidity": humidity_data,
        "categories": categories
    }

    smog_data = {
        "pm10": pm10_data,
        "pm25": pm25_data,
        "categories": categories
    }

    return smog_data, weather_data


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('get_initial_data')
def handle_event(data):
    smog_data, weather_data = prepare_data()
    data = {
        'smog_data': smog_data,
        'weather_data': weather_data,
        'colors': {
            'first': FIRST_COLOR,
            'second': SECOND_COLOR
        }
    }
    emit('initial_data', data)


@app.route('/api/<pm10>/<pm25>/<temperature>/<humidity>', methods=['GET'])
def dust_and_temperature(pm10, pm25, temperature, humidity):
    if all([pm10, pm25, temperature, humidity]):
        smog_data = SmogMetric(
            pm10=float(pm10),
            pm25=float(pm25),
            temperature=float(temperature),
            humidity=float(humidity)
        )
        db.session.add(smog_data)
        db.session.commit()

    smog_data, weather_data = prepare_data()

    socketio.emit('weather', weather_data)
    socketio.emit('smog', smog_data)

    return redirect(url_for('index'))


# @app.route('/api/t/<temperature>/<humidity>', methods=['GET'])
# def temperature(temperature, humidity):
#     return redirect(url_for('index'))
