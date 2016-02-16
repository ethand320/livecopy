import socket

def startServer():
    print("Starting server...")
    s = socket.socket()
    host = socket.gethostname()
    port = 2423
    s.bind((host, port))
    s.listen(5)
    c, addr = s.accept()
    while True:
        
        val = c.recv(1024)
        print("Server has received: " + val.decode("utf-8"))
        
        
