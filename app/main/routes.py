import namegenerator
from flask import url_for, render_template, request, jsonify, redirect

from app.controllers.room_manager import RoomManager
from app.models.roles import Roles
from app.models.user import User
from .. import flaskapp

room_manager = RoomManager()
print("Création du RoomManager...")


@flaskapp.route('/')
def show_index():
    generated_pseudo = namegenerator.gen()
    user_ip_address = request.remote_addr
    user = User(generated_pseudo, user_ip_address, Roles.CREATOR)

    generated_room_id = room_manager.add_new_room__(user)
    print("Création de la room %d." % generated_room_id, end="\n\n")

    return redirect(url_for('show_room_page', room_id=generated_room_id))


@flaskapp.route('/rooms/<int:room_id>')
def show_room_page(room_id):
    if room_manager.check_room(room_id) is False:
        print("Un user a tenté d'accéder a une room inexistante (%d). Redirection vers la racine..." % room_id,
              end="\n\n")
        return redirect(url_for('show_index'))

    current_user = connect_to_existing_room(room_id, request.remote_addr)

    room_users = room_manager.get_room_list()[room_id].get_userlist()

    template_args = {'style_index_url': url_for('static', filename='styles/index.css'),
                     'scripts_index_url': url_for('static', filename='scripts/index.js'),
                     'default_user_img': url_for('static', filename='res/img/defaultUser.png'),
                     'no_video_img': url_for('static', filename='res/img/noVideoImg.png'),
                     'users': room_users,
                     'current_user': current_user,
                     'roomID': room_id
                     }

    return render_template('index.html', template_args=template_args)


@flaskapp.route('/rooms/<int:room_id>/population')
def give_room_population(room_id):
    json_str = room_manager.get_room_list()[room_id].get_json_username_list()
    return jsonify(json_str)


def connect_to_existing_room(room_id, ip_address):
    user = None
    if not room_manager.get_room_list()[room_id].get_creator_connected_state():
        user = room_manager.get_room_list()[room_id].get_creator()
        room_manager.get_room_list()[room_id].set_creator_connected_state(True)
    else:
        pseudo = namegenerator.gen()
        user = User(pseudo, ip_address, Roles.LAMBDA)
        room_manager.get_room_list()[room_id].add_new_user(user)

    print("Nouvelle connection à la room {%s} : login[%s] - ip[%s] - role[%s]" % (
        str(room_id), user.get_pseudo(), user.get_ip_address(), user.get_role().name))
    return user