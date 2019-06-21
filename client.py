import socket
import math
import time
UDP_DEFAULT_BUFFER_SIZE = 8000
UDP_HEADER_SIZE = 42
class Client:

    def __init__(self, args):
        self.ip = args.i
        self.port = args.p
        self.rate = math.ceil(args.r * 1000 / 8)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.packetsPerSecond = math.ceil(self.rate / UDP_DEFAULT_BUFFER_SIZE)
        self.lastMessageLength = self.rate - ((self.packetsPerSecond - 1) * UDP_DEFAULT_BUFFER_SIZE)

        self.message = bytearray(UDP_DEFAULT_BUFFER_SIZE - UDP_HEADER_SIZE)
        self.lastMessage = bytearray(0)
        if self.lastMessageLength > UDP_HEADER_SIZE:
            self.lastMessage = bytearray(self.lastMessageLength - UDP_HEADER_SIZE)
        

    def start(self):
        while True:
            timeToWait = 1.0 / float(self.packetsPerSecond)
            remaningTime = 1.0
            for packet in range(0, self.packetsPerSecond - 1):
                partialTimeBegin = time.time()
                self.socket.sendto(self.message, (self.ip, self.port))
                partialTimeEnd = time.time()
                partialElapsedTime = partialTimeEnd - partialTimeBegin 
                
                time.sleep(timeToWait - partialElapsedTime)
                endTime = time.time()
                remaningTime = remaningTime - endTime + partialTimeBegin
                timeToWait = remaningTime/(self.packetsPerSecond - packet)
                

            if self.lastMessageLength != 0:
                time.sleep(timeToWait)
                timeBegin = time.time()
                self.socket.sendto(self.lastMessage, (self.ip, self.port))
                timeEnd = time.time()
                elapsedTime = timeEnd - timeBegin 
                time.sleep(timeToWait)

            print("Sent", self.rate * 8 / 1000000, "Mbit/s")
