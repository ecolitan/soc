import socket
import sys
import uuid
import json
    
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

    def send_request(self, request):
        """Send request to gameserver
        Return reply
        """
        
        try:
            # Connect to server and send data
            self.sock.connect((self.HOST, self.PORT))
            self.sock.sendall(request)

            # Receive data from the server and shut down
            received = self.sock.recv(1024)
        finally:
            self.sock.close()

        print "Sent:     {}".format(request)
        print "Received: {}".format(received)
        
        return received
        
    def generate_request(self):
        """generate a request"""
        return str({"uuid", self.client_id})

if __name__ == "__main__":
    client = GameClient()
    request = client.generate_request()
    client.send_request(request)
    
        
