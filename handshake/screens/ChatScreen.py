import tkinter as tk

import requests
from handshake import ACCENT, LIGHT_FG, SERVER_URL, WHITE

from handshake.utils import get_active_user_count, join_chatroom

class ChatScreen(tk.Frame):

    username: str = ''

    def __init__(self,parent, controller):
        super().__init__(parent)
        join_chatroom(ChatScreen.username)


        self.chat_box = tk.Text(self, state='disabled')
        self.chat_box.config(bg='#181818', fg=WHITE)
        self.chat_box.grid(column=0,row=0, columnspan=2, sticky="ew")

        self.entry = tk.Entry(self)
        self.entry.grid(column=0,row=1, columnspan=2, sticky="ew")
        
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.config(bg='#181818',fg=LIGHT_FG)
        self.send_button.grid(column=0, row=2, sticky="ew")

        users = f'Users: {get_active_user_count()}'
        self.refresh_button = tk.Label(self, text=users)
        self.refresh_button.config(bg=ACCENT,fg=LIGHT_FG)
        self.refresh_button.grid(column=1, row=2, sticky="ew")

        self.after(250, self.get_messages)
        

    def poll_messages(self):
        self.get_messages()

    def send_message(self):
        message = f'{ChatScreen.username}: {self.entry.get()}'
        if self.entry.get():
            requests.post(f"{SERVER_URL}/send", json={"message": message})
            self.entry.delete(0, tk.END)
            self.get_messages()

    def get_messages(self):
        response = requests.get(f"{SERVER_URL}/messages")
        messages = response.json()
        self.chat_box.configure(state='normal')
        self.chat_box.delete(1.0, tk.END)
        for msg in messages:
            self.chat_box.insert(tk.END, msg + "\n")
        self.chat_box.configure(state='disabled')
        self.after(250, self.poll_messages)


