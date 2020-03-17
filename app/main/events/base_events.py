from flask_socketio import join_room

from app import socket_io
from . import sockets_rooms
from .update_lists_orders import *
from ..routes.routes import room_manager


@socket_io.on('message')
def new_socket_connection_handler(message):
    str = "Message réçu d'un socket -> " + message
    print(str, end="\n\n")
    emit('reponse', str)


@socket_io.on('json')
def handle_socket_json(json):
    print("json reçu d'un socket -> \n" + str(json), end="\n\n")
