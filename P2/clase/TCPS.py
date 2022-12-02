from socket import *
from MMST import *

class TCPServer():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.__socket = None

    def connect(self):
        self.__socket = socket(AF_INET. SOCK_STREAM)
        self.__socket.bind((self.host. self.port))
        self.__socket.listen(1)

    def disconect(self):
        self.__socket.close()
        self.__socket = None

    def getSocket(self):
        return self.__socket

    def communication(self):
        while True:
            cliente, direccion = self.__socket
            print("Conexión desde:", direccion)
            socketCliente = MMST(cliente, direccion)
            socketCliente.start