from handshake import Server

if __name__ == '__main__':
    server = Server.create_instance()
    server.run(debug=True)

