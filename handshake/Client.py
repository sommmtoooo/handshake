import tkinter as tk
from handshake.screens import ChatScreen
from handshake.screens import HomeScreen


class HandShakeClient(tk.Tk):
    screens  = ([ChatScreen, HomeScreen])
    instance = None

    @staticmethod
    def getInstance():
        if not HandShakeClient.instance:
            return HandShakeClient()
        return HandShakeClient.instance


    def __init__(self):
        super().__init__()
        self.title("Handshake")

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


