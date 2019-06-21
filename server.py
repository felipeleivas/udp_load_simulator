import socket
import threading
UDP_DEFAULT_BUFFER_SIZE = 8000

class Server:

    def __init__(self, args):
        self.port = args.p
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.getOwnIpAdress(), self.port))
        

    def start(self):
        while True:
            data, address = self.socket.recvfrom(UDP_DEFAULT_BUFFER_SIZE)
            print("Recive",len(data))
            

    def getOwnIpAdress(self):
        temporarySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temporarySocket.connect(("8.8.8.8", 80))
        ownIp = temporarySocket.getsockname()[0]
        temporarySocket.close()
        print(ownIp)
        return ownIp