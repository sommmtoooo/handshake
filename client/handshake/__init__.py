SERVER_URL = 'http://127.0.0.1:5000'
LIGHT_FG = '#FFFFAD'
DARK = '#181818'
WHITE = '#FAFAFA'
LIGHT_BG = '#FA0FA9'
ACCENT = '#A1A1A1'

from handshake.Client import HandShakeClient

def run_instance():
    client = HandShakeClient.getInstance()
    client.mainloop()
