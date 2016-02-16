import time
import socket

def launchReader(filename):
    print("Connecting to server...")
    connectToServer()
    print("Opening log file " + str(filename))
    logfile = open(filename)
    loglines = follow(logfile)
    ## logic to send to server here
    print("Writing Stream to server")
    for line in loglines:
        
        writeLineToServer(line)
        


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
def connectToServer():
    
    host = socket.gethostname()
    port = 2423
    s.connect((host, port))
    print("connection made, ready...")


"""
logfile = open("run/foo/access-log","r")
    loglines = follow(logfile)
    for line in loglines:
        print line,
        """

def writeListToServer(lines):
    for line in lines:
        s.send(bytes(line, 'utf-8'))



def closeConnectionToServer(s):
    
    s.close


def writeLineToServer(line):
    try:
        s.send(bytes(line, 'utf-8'))

    except Exception as e:
        print("error writing to server")
        

