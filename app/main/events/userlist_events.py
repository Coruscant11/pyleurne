from flask import request
from flask_socketio import join_room, emit

from ..routes.routes import room_manager
from .base_events import sockets_rooms
from .update_lists_orders import *

from app import socket_io


@socket_io.on('join')
def on_join(data):
    username = data['username']
    room = int(data['room'])
    join_room(room)

    print("\t\t -> (%s) connecté à la room de sockets (%s) " % (username, room), end="\n\n")
    emit('join', 'Vous rejoignez la room %s' % room)

    if room not in sockets_rooms:
        sockets_rooms[room] = []
        sockets_rooms[room].append(username)
    else:
        sockets_rooms[room].append(username)

    tell_to_users_to_update_userlist(room)
    tell_to_users_to_update_playlist(room)
