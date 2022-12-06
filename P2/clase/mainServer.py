import TCPS as TCPS

if __name__ == '__main__':
    socketServer = TCPS.TCPServer('localhost', 15008)
    socketServer.connect()
    socketServer.communication()