import socket
import sys
import threading
def startServer():
    print("Starting server...")
    s = socket.socket()
    host = socket.gethostname()
    port = 2423
    s.bind((host, port))
    s.listen(5)
    c, addr = s.accept()
"""
    while True:
        
        val = c.recv(1024)
        print("Server has received: " + val.decode("utf-8"))
    """     


class Server:
    def __init__(self):
        self.host = ''
        self.port = 2423
        self.backlog = 10
        self.size = 1024 #need?
        self.server = None
        self.threads = []  # for storing all threads

    def openSocket(self):
        try:
            self.server = socket.socket()
            self.server.bind((self.host, self.port))
            self.server.listen(5)
            print("Server Listening on port: " + str(self.port))
        except socket.error  (value, message):
            if self.server:
                 self.server.close()   #if a server obj exists close i
            print("Error couldn't open socket " + message)
            
    def run(self):
        self.openSocket()
        while True:
            print("waiting for client to connect..")
            conn, addr = self.server.accept()
            print("client connected!")
            c = Client(conn, addr)
            c.start()
            self.threads.append(c)
        
import datetime




class Client(threading.Thread):
    def __init__(self, client, address ):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024
        

    def run(self):
        print("strating thread for client connection...")
        running = 1
        
        while running:
            print("server waiting for data...")
            data = self.client.recv(self.size)
            if data:
                ### we've received data
                ## if starts with FILETOSAVE, create a new file 
                if data.startswith(bytes('FILENAMETOSAVE:', 'utf-8') ):
                    ##create new file for writing.
                    today = str(datetime.date.today())
                    myfile = data.decode('utf-8').partition('!')[0]
                    myfile = myfile[15:]
                    print("decoded myfile = " + myfile)
                    
                    file = open(myfile + today + ".copy", 'a', 1)
                    print(data.decode('utf-8').partition('!')[2])
                    file.write(data.decode('utf-8').partition('!')[2])
                    
                else:
                    if file:
                        print("writing line to file...")
                        
                        file.write(data.decode('utf-8'))
                        
            else:
                if file:
                    file.close()
                print("No more data... closing")
                self.client.close()
                running = 0




####### main method to kick off server
if __name__ == "__main__":
    s = Server()
    s.run()

