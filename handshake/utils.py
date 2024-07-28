from . import SERVER_URL
import requests

def join_chatroom(username):
    resp = requests.post(f"{SERVER_URL}/active", json={"username": username})
    return "Welcome" 

def get_active_user_count():
    resp = requests.get(f"{SERVER_URL}/members")
    return resp.json()['members']
