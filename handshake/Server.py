from flask import Flask, request, jsonify
from flask_cors import CORS


def create_instance():
    app = Flask(__name__)
    CORS(app)
    
    messages = []

    @app.route('/')
    def index():
        return 'Handshake'
    
    @app.route('/send', methods=['POST'])
    def send_message():
        data = request.get_json()
        messages.append(data['message'])
        return jsonify({"status": "Message received"})
    
    @app.route('/messages', methods=['GET'])
    def get_messages():
        return jsonify(messages)
    
    return app
    if __name__ == '__main__':
        app.run(debug=True)
