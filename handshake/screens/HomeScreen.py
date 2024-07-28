import tkinter as tk

import requests
from handshake import SERVER_URL
from handshake.screens.ChatScreen import ChatScreen

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.config(padx=10, pady=10)
        self.error_msg = tk.StringVar()

        self.title = tk.Label(self, text="Welcome to Handshake")
        self.title.config(font=('DM Sans', 20), anchor='center')
        self.title.grid(row=0, column=0, columnspan=2, sticky=tk.EW)

        self.username = tk.Entry(self)
        self.username.grid(row=1, column=0, columnspan=2, sticky=tk.EW)

        enter_btn = tk.Button(self, text="Enter",
                            command=self.switch_to_chat_frame)
        enter_btn.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

        self.error_label = tk.Label(self, textvariable=self.error_msg)
        self.error_label.config(fg='red');
        self.error_label.grid(row=3, column=0, columnspan=2, sticky=tk.EW)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def switch_to_chat_frame(self):
        if self.username.get() == '':
            print('Empty')
            self.error_msg.set('Username Cannot Be Empty')
            return
        requests.post(f"{SERVER_URL}/join", json={"username": self.username.get()})
        message = ("User Joined: " + self.username.get())
        requests.post(f"{SERVER_URL}/send", json={"message": message})
        ChatScreen.username = self.username.get()
        self.controller.show_frame("ChatScreen")


