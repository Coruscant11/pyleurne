from flask_socketio import join_room, emit

from ..routes.routes import room_manager
from .base_events import sockets_rooms
from .update_lists_orders import *

from app import socket_io


@socket_io.on('videoAddRequest')
def handle_video_add_request(data):
    room_id = int(data['room'])
    username = data['username']
    video_url = data['videoURL']
    user_caller = room_manager.get_room_list()[room_id].get_userlist()[username]

    print("Demande d'ajout de vidéo reçue. Voici les détails :", end="\n\t")
    print("username[%s]" % username, "room[%d]" % room_id, "videoURL[%s]" % video_url, sep="\n\t")

    print("Est-ce demandé par le créateur : ", end="")
    print(user_caller == room_manager.get_room_list()[room_id].get_creator(), end="\n\n")

    if room_manager.get_room_list()[room_id].get_playlist_manager().add_video(video_url, user_caller):
        tell_to_users_to_update_playlist(room_id)

    emit('videoValidation', 'Demande reçue l\'ami.')
