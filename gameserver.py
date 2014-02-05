import select
import socket
import sys
import threading

class GameServer:
    def __init__(self):
        self.host = ''
        self.port = 9000
        self.backlog = 5
        self.size = 2048
        self.server = None
        self.threads = []

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind((self.host,self.port))
            self.server.listen(5)
        except socket.error, (value,message):
            if self.server:
                self.server.close()
            print "Could not open socket: " + message
            sys.exit(1)

    def run(self):
        self.open_socket()
        input = [self.server,sys.stdin]
        running = 1
        while running:
            inputready,outputready,exceptready = select.select(input,[],[])
            for s in inputready:
                if s == self.server:
                    # handle the server socket
                    c = ClientThread(self.server.accept())
                    c.start()
                    self.threads.append(c)

                elif s == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = 0
        # close all threads
        for c in self.threads:
            c.join()

class ClientThread(threading.Thread):
    
    request_terminator = '\r\n\r\n'
    
    def __init__(self, (client,address)):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 2048
        self.request_queue = ''

    def run(self):
        running = True
        while running:
            data = self.client.recv(self.size)
            if data:
                self.request_queue += data
                self.process_request()
            else:
                self.client.close()
                running = False
                
    def process_request(self):
        """Do something with the informtion from the client."""
        pass
        
    def pop_next_request(self):
        """Return first request in request queue
        request is removed from the queue
        return None if no valid request
        """
        request_end = self.request_queue.find(self.request_terminator)
        if request_end == -1:
            next_request = None
        else:
            next_request = self.request_queue[:request_end + len(self.request_terminator)]
            self.request_queue = self.request_queue[request_end + len(self.request_terminator):]
            
        return next_request
        
    def queue_contains_request(self):
        """return True if queue contains a request"""
        
        request_end = self.request_queue.find(self.request_terminator)
        if request_end == -1:
            request_exists = False
        else:
            request_exists = True
            
        return request_exists

def main():
    s = GameServer()
    s.run()
    sys.exit(3)
    
if __name__ == "__main__":
    main()
