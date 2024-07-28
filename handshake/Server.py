import time
from os import abort
from flask import Flask, request, jsonify
from flask_cors import CORS


def create_instance():
    app = Flask(__name__)
    CORS(app)
    
    messages = []
    users = []


    @app.route('/')
    def index():
        return 'Handshake'


    @app.post('/join')
    def join_room():
        data = request.get_json()
        username = data['username']
        users.append(username)
        return jsonify({
            'message': 'Welcome'
            })


    @app.get('/members')
    def members():
        return jsonify({"members": len(users)})


    @app.post('/exit')
    def exit_room():
        data = request.get_json()
        users.remove(data['username'])
        return jsonify({"active_users": len(users)})

    
    @app.route('/send', methods=['POST'])
    def send_message():
        data = request.get_json()
        messages.append(data['message'])
        return jsonify({"status": "Message received"})
    

    @app.route('/messages', methods=['GET'])
    def get_messages():
        return jsonify(messages)
    
    return app

