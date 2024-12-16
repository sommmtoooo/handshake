from os import abort, name
from flask import Flask
# from flask_socketio import Namespace, SocketIO

app = Flask(__name__)
# socky = SocketIO(app)

messages = []
users = []


@app.route('/')
def index():
    return 'Handshake'


app.run(debug=True)
