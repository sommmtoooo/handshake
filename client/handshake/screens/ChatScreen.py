import tkinter as tk

from handshake import ACCENT, LIGHT_FG, WHITE

class ChatScreen(tk.Frame):

    username: str = ''

    def __init__(self,parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.chat_box = tk.Text(self, state='disabled')
        self.chat_box.config(bg='#181818', fg=WHITE)
        self.chat_box.grid(column=0,row=0, columnspan=2, sticky="ew")

        self.entry = tk.Entry(self)
        self.entry.grid(column=0,row=1, columnspan=2, sticky="ew")
        self.entry.bind('<Return>', self.send_message)
        
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.config(bg='#181818',fg=LIGHT_FG)
        self.send_button.grid(column=0, row=2, sticky="ew")

        users = f'Users: {0}'
        self.refresh_button = tk.Label(self, text=users)
        self.refresh_button.config(bg=ACCENT,fg=LIGHT_FG)
        self.refresh_button.grid(column=1, row=2, sticky="ew")

    def send_message(self, event=None):
        if self.entry.get():
            self.entry.delete(0, tk.END)

    def get_messages(self, message):
        self.chat_box.configure(state='normal')
        self.chat_box.insert(tk.END, message + '\n')
        self.chat_box.configure(state='disabled')
        self.chat_box.yview(tk.END)

