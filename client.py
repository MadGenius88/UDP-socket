# Receiver
import socket

HOST = "localhost"
PORT = 5454

# Set up receiving socket UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind( (HOST,PORT) )

# Receive and print data
while 2:
    data = udp_socket.recv(30)
    print(data)


import socket
import time
import pickle

Type=100 #message type can be up to 255 =1byte
ignore=0#the seconnecbyte has no significan represntation
time=2 #specify a time data can be up to 6000 sec =2bytes
ID=101 #ID  4bytes
Datasend=[Type,ignore,time,ID]
Datasend = pickle.dumps(Datasend)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def TCPconnection():
    print "trying to set a Tcp sesion"
    clientsocket2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            clientsocket2.connect((socket.gethostname(),5000))
            data=clientsocket2.recv(1024)
            print "Recived a TCP response from server",data
            clientsocket2.send("thank you server")
            clientsocket2.close()
            break
        except Exception as e:
            print ("try again...reason",e)

while True:
    clientsocket.sendto(Datasend,(socket.gethostname(),4449))
    clientsocket.settimeout(1)
    try:
        DATA,addr=clientsocket.recvfrom(1024)
        if DATA:
            print"Recived response from server:",DATA
            if DATA=="connection accepted":
                clientsocket.close()
                TCPconnection()
                break
            else:
                print"connection refused closing"

        clientsocket.close()
        break
    except Exception as e:
        print ("try again ..reason:",e)
