'''
from flask import Flask
from .views import app, socket_io
'''

from flask import Flask
from flask_socketio import SocketIO

flaskapp = Flask(__name__, instance_relative_config=True)
socket_io = SocketIO()

def create_app(debug=False):
    flaskapp.config.from_object('config')
    flaskapp.debug = debug

    import app.main.routes
    import app.main.events

    socket_io.init_app(flaskapp)
    return flaskapp