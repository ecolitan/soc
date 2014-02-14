import SocketServer
import time
import threading
from player import BasePlayer
from clientrequest import ClientRequest

class ThreadedTCPRequestHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        """The request handler"""
        while True:
            self.data = self.request.recv(1024)
            if self.data:
                cur_thread = threading.current_thread()
                response = "{}: {}".format(cur_thread.name, self.data)
                self.request.sendall(response)
            #~ time.sleep(1)    

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever())
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    
