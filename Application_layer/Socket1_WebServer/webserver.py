#!/usr/bin/env python
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
#prepare a server socket
serverSocket.bind(('',6789))
serverSocket.listen(1)
while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Send on the HTTP header line into socket
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' %(len(outputdata))
        connectionSocket.send(header.encode())
        #Send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print("OK!")
    except IOError as e:
        #Send reponse message for file not found
        header = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
        connectionSocket.send(header.encode())
        #Close client socket
        #for i in range(0,len(outputdata)):
            #connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
serverSocket.close()
