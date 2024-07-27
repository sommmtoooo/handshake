import tkinter as tk
import requests

LIGHT_FG = '#FFFFAD'
DARK = '#181818'
WHITE = '#FAFAFA'
LIGHT_BG = '#FA0FA9'
ACCENT = '#A1A1A1'


class ChatScreen(tk.Frame):

    def __init__(self,parent, controller):
        super().__init__(parent)

        self.chat_box = tk.Text(self, state='disabled')
        self.chat_box.config(bg='#181818', fg=WHITE)
        self.chat_box.grid(column=0,row=0, columnspan=2, sticky="ew")

        self.entry = tk.Entry(self)
        self.entry.grid(column=0,row=1, columnspan=2, sticky="ew")
        
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.config(bg='#181818',fg=LIGHT_FG)
        self.send_button.grid(column=0, row=2, sticky="ew")

        self.refresh_button = tk.Button(self, text="Refresh", command=self.get_messages)
        self.refresh_button.config(bg=ACCENT,fg=LIGHT_FG)
        self.refresh_button.grid(column=1, row=2, sticky="ew")

        self.server_url = 'http://127.0.0.1:5000'
        self.after(250, self.get_messages)
        


    def poll_messages(self):
        self.get_messages()

    def send_message(self):
        message = self.entry.get()
        if message:
            requests.post(f"{self.server_url}/send", json={"message": message})
            self.entry.delete(0, tk.END)
            self.get_messages()

    def get_messages(self):
        response = requests.get(f"{self.server_url}/messages")
        messages = response.json()
        self.chat_box.configure(state='normal')
        self.chat_box.delete(1.0, tk.END)
        for msg in messages:
            self.chat_box.insert(tk.END, msg + "\n")
        self.chat_box.configure(state='disabled')
        self.after(250, self.poll_messages)


class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.config(padx=10, pady=10)

        title = tk.Label(self, text="Welcome to Handshake")
        title.config(font=('DM Sans', 20), anchor='center')
        title.grid(row=0, column=0, columnspan=2, sticky=tk.EW)

        username = tk.Entry(self)
        username.grid(row=1, column=0, columnspan=2, sticky=tk.EW)

        button1 = tk.Button(self, text="Enter",
                            command=lambda: controller.show_frame("ChatScreen"))
        button1.grid(row=2, column=0, columnspan=2, sticky=tk.EW)


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)


class HandShakeClient(tk.Tk):
    screens  = ([ChatScreen, HomeScreen])

    def __init__(self):
        super().__init__()
        self.title("Chat Client")

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0,sticky=tk.NSEW)


        self.frames = {}
        self.create_frames()

    def create_frames(self):
        for F in HandShakeClient.screens:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row="0", column="0", sticky=tk.NSEW)

        self.show_frame("HomeScreen")


    def show_frame(self, screen):
        frame = self.frames[screen]
        frame.tkraise()




