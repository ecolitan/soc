import SocketServer
import uuid
import time
from player import BasePlayer
from clientrequest import ClientRequest

class MyTCPHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        """The request handler"""
        while True:
            self.data = self.request.recv(1024).strip()
            print "Received:    {}".format(self.data)
            self.request.sendall(self.data.upper())
            print "Sent:        {}".format(self.data.upper())
            time.sleep(1)
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    a = 0
    # Create the server, binding to localhost on port 9999
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    player_list =  []

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
