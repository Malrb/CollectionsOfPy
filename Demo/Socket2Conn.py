# Run this on the PC that want to check if other PC is online.
from socket import *

def pingit():                               # defining function for later use

    s = socket(AF_INET, SOCK_STREAM)         # Creates socket
    host = 'localhost' # Enter the IP of the workstation here 
    port = 80                # Select port which should be pinged

    try:
        s.connect((host, port))    # tries to connect to the host
    except ConnectionRefusedError: # if failed to connect
        print("Server offline")    # it prints that server is offline
        s.close()                  #closes socket, so it can be re-used
        pingit()                   # restarts whole process    

    while True:                    #If connected to host
        print("Connected!")        # prints message 
        s.close()                  # closes socket just in case
        exit()                     # exits program

/* Main Startup */
pingit()                           #Starts off whole process




# this runs on remote pc that is going to be checked
from socket import *

HOST = 'localhost'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
serversock = socket(AF_INET, SOCK_STREAM)
serversock.bind(ADDR)
serversock.listen(2)

while 1:
    clientsock, addr = serversock.accept()
    serversock.close()
    exit()
