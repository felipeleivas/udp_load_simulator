import sys
import clientParser
import client
import server

parser = clientParser.ClientParser()

def main():
    args = parser.getArgs()
    if args.i != None and args.p != None and args.r != None:        
        print("Starting Client")
        c = client.Client(args)
        c.start()
    elif args.p != None:     
        print("Starting Server")
        s = server.Server(args)
        s.start()
    else:
        print("Usage: -p serverPort -i serverAddress -r bandwidth")

if __name__ == '__main__':
    main()
    