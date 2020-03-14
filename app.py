from flask import Flask, url_for, escape, render_template, request, jsonify

userAdmin = 'Coruscant11'
userPassword = 'antoineCHIBREdu93'

app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template('index.html', style_index_url=url_for('static', filename='styles/index.css'),
                           script_index_url=url_for('static', filename='scripts/index.js'))


@app.route('/rooms', methods=['GET', 'POST'])
def show_room_page(roomID):
    if request.method == 'POST':
        try:
            userName = request.form['username']
            print("L'utilisateur [%s] demande la création d'une room." % userName)

            return render_template('rooms.html', user_name=userName)
        except:
            print('ERREUR DURANT LA RECEPTION DE LA METHODE POST DE CREATION DE ROOM.')


    elif request.method == 'GET':
        return


if __name__ == '__main__':
    app.run()
