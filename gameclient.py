import socket
import sys
import uuid
import time

class GameClient:
    """example client"""
    
    def __init__(self):
        # Each client has a unique id string
        self.client_id = str(uuid.uuid4())
        #TODO client config file
        self.HOST = "localhost"
        self.PORT = 9999
        # Create a socket (SOCK_STREAM means a TCP socket)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.HOST, self.PORT))

    def send_request(self, request):
        """Send request to gameserver
        Return reply
        """
        
        try:
            # Connect to server and send data
            
            self.sock.sendall(request)

            # Receive data from the server and shut down
            received = self.sock.recv(1024)
        finally:
            #~ self.sock.close()
            pass

        print "Sent:     {}".format(request)
        print "Received: {}".format(received)
        
        return received
        
    def generate_request(self):
        """generate a request"""
        return str(self.client_id)
        #~ return str({"uuid", self.client_id})
        
    def close(self):
        self.sock.close()

if __name__ == "__main__":
    client = GameClient()
    #~ request = client.generate_request()
    client.connect()
    #~ client.send_request(request)
    #~ time.sleep(2)
    #~ client.send_request(request)
    request = raw_input("> ")
    while request.lower() not in ["exit", "quit"]:
        client.send_request(request)
        request = raw_input("> ")
    client.close()
