import time 
import socket

def logwriter():
    #startServer()
    n = 1
    while True:
        f = open('logfile.txt.', 'a')
        f.write("hello " + str(n) + "\n")
        n += 1
        f.close()
        time.sleep(.1)



