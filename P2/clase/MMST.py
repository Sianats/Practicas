import threading
import random

class MMST(threading.Thread):

    def __init__(self, client_socket, client_addr):
        threading.Thread.__init__(self)
        self.__client_socket = client_socket
        self.__client_addr = client_addr
        self.end = False

    def run(self):
        try:
            while not self.end:
                msg = self.__client_socket.recv(1024).decode()
                resp = "Holii"
                self.__client_socket.send(resp.encode())
            
        except ConnectionAbortedError:
            print ("Conexión Cerrada")
            self.end = True
