from flask import url_for
from flask_socketio import emit

from .base_events import sockets_rooms
from ..routes.routes import room_manager


def tell_to_users_to_update_userlist(room):
    print("Emit d'ordre de refresh userlist pour room[%s]..." % (room))
    emit('clearuserlist', 'Rafraichissement userlist', room=room)

    for i in sockets_rooms[room]:
        url = url_for('static', filename='res/img/defaultUser.png')
        print("emit -> (%s), (%s)" % (i, url))
        emit('appendUser', (i, url), room=room)

    print("")


def tell_to_users_to_update_playlist(room_id):
    print("Emit d'ordre de refresh playlist pour room[%s]..." % (room_id))
    emit('clearplaylist', "Rafraichissement playlist", room=room_id)

    for i in room_manager.get_room_list()[room_id].get_playlist_manager().get_playlist():
        video_url = i.get_video_url()
        video_id = i.get_video_id()
        caller = i.get_caller()

        print("\tEmit -> (%s), (%s), (%s)" % (video_url, video_id, caller))
        emit('appendVideo', (video_url, video_id, caller.get_pseudo()), room=room_id)

    print("")
