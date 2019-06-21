import argparse
import sys

class ClientParser:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", help="Server IP", type=str)
        parser.add_argument("-p", help="Server Port", type=int)
        parser.add_argument("-r", help="Bandwidth", type=int)
        self.args = parser.parse_args()

    def getArgs(self):
        return self.args
