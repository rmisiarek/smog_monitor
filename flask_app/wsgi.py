from smog_monitor import create_app


app, socketio = create_app()

#if __name__ == '__main__':
socketio.run(app=app, host='192.168.0.129', port='5555', debug=True)
#socketio.run(app, debug=True)
