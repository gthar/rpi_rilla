import time
import socket
from rpi_rilla.threadable import Threadable
from rpi_rilla.socket_sender import send_msg

sep = "_"

class SocketHandler(Threadable):
    def __init__(self, action, port=10000, host='127.0.0.1', max_length=4096):
        self.action = action
        self.max_length = max_length
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(10)
        super().__init__()

    def loop(self):
        client_socket, _ = self.server_socket.accept()
        msg = client_socket.recv(self.max_length).decode()
        cmds = msg.split(sep)
        print(cmds)

        try:
            f = self.action(*cmds)
        except TypeError:
            f = None
        if f is None:
            print("no action implemented for this message")
        else:
            f()

    def self_send(self, msg):
        send_msg(msg, self.host, self.port)

    def stop(self):
        super().stop()
        self.self_send("_")
        self.server_socket.close()
