from flask import Flask, url_for, escape, render_template, request, jsonify, redirect
from flask_socketio import SocketIO, join_room, leave_room, send, emit

from .routes import room_manager
from .. import socket_io



sockets_rooms = {}
print("Création de la liste des room des sockets...")


@socket_io.on('message')
def new_socket_connection_handler(message):
    str = "Message réçu d'un socket -> " + message
    print(str, end="\n\n")
    emit('reponse', str)


@socket_io.on('json')
def handle_socket_json(json):
    print("json reçu d'un socket -> \n" + str(json), end="\n\n")


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


def tell_to_users_to_update_userlist(room):
    print("\nEmit d'ordre de refresh userlist pour room[%s][%s]..." % (room, type(room)))
    emit('clearuserlist', 'Rafraichissement userlist', room=room)

    for i in sockets_rooms[room]:
        url = url_for('static', filename='res/img/defaultUser.png')
        print("emit -> (%s), (%s)" % (i, url))
        emit('appendUser', (i, url), room=room)

    print("")


''' PARTIE AJOUT DE VIDEO '''


@socket_io.on('videoAddRequest')
def handle_video_add_request(data):
    room_id = int(data['room'])
    username = data['username']
    video_url = data['videoURL']
    userCaller = room_manager.get_room_list()[room_id].get_userlist()[username]

    print("Demande d'ajout de vidéo reçue. Voici les détails :", end="\n\t")
    print("username[%s]" % username, "room[%d]" % room_id, "videoURL[%s]" % video_url, sep="\n\t")

    print("Est-ce demandé par le créateur : ", end="")
    print(userCaller == room_manager.get_room_list()[room_id].get_creator(), end="\n\n")

    if room_manager.get_room_list()[room_id].get_playlist_manager().add_video(video_url, userCaller):
        tell_to_users_to_update_playlist(room_id)

    emit('videoValidation', 'Demande reçue l\'ami.')


def tell_to_users_to_update_playlist(room_id):
    print("\nEmit d'ordre de refresh playlist pour room[%s][%s]..." % (room_id, type(room_id)))
    emit('clearplaylist', "Rafraichissement playlist", room=room_id)

    for i in room_manager.get_room_list()[room_id].get_playlist_manager().get_playlist():
        video_url = i.get_video_url()
        video_id = i.get_video_id()
        caller = i.get_caller()

        print("\tEmit -> (%s), (%s), (%s)" % (video_url, video_id, caller))
        emit('appendVideo', (video_url, video_id, caller.get_pseudo()), room=room_id)

    print("")
