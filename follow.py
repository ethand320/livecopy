import time
import socket

def launchReader(filename):
    print("Connecting to server...")
    connectToServer(filename)
    print("Opening log file " + str(filename))
    logfile = open(filename)
    loglines = follow(logfile)
    ## logic to send to server here
    print("Writing Stream to server")
    try:
        
        for line in loglines:
            
            writeLineToServer(line)
    except (KeyboardInterrupt, SystemExit):
        
        print("Done writing, closing connection")
        s.close()
    


def follow(thefile):
    thefile.seek(0)
    while True:
        line = thefile.readline()
        #print(line)
        if not line:
            time.sleep(0.1)
            continue
        print("called writeline")
        yield line

s = socket.socket()
def connectToServer(filename):
    
    #host = socket.gethostname()
    host = "162.243.65.65"
    port = 2423
    s.connect((host, port))
    print("connection made, ready...")
    serverinit = "FILENAMETOSAVE:"+ filename + "!"
    s.send(bytes(serverinit, 'utf-8'))
    

"""
logfile = open("run/foo/access-log","r")
    loglines = follow(logfile)
    for line in loglines:
        print line,
        """


def closeConnectionToServer(s):
    
    s.close


def writeLineToServer(line):
    try:
        s.send(bytes(line, 'utf-8'))

    except Exception as e:
        print("error writing to server")
        

if __name__ == "__main__":
    file = input("enter filename to livecopy: ")
    launchReader(file)
    
    
