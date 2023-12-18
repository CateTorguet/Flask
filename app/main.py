import flask
import socket
import os
n_visitas=0

APP = flask.Flask(__name__)

@APP.route('/')
def index():

    userinfo = {
            'user': os.environ['CLIENT_NAME'],
            'apellido': 'Castillo'
            }
    global n_visitas
    n_visitas = n_visitas + 5
    hostname = socket.gethostname()
    return flask.render_template('index.html', user=userinfo, n_visitas=n_visitas, server=hostname)

if __name__ == '__main__':
    PORT=os.environ['PORT']
    APP.debug = True
    APP.run(host='0.0.0.0', port=PORT)
