# Sender
import socket
import time

HOST = "localhost"
PORT = "5454"
data = "It always seems impossible until it's done - Nelson Mandela"

# Set up our sending socket UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind( (HOST,PORT) )

# Send greeting to the receiver
while 2:
    s.sendto(data,(HOST<PORT))
    print "sent: "+data
    time.sleep(1)

import socket
import pickle
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind((socket.gethostname(),4449))
serversocket.settimeout(1)
Datasend=('connection accepted')
#msg = bytearray()

def TCPconnection ():
    print "trying to start a tcp session"
    serversocket2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serversocket2.bind((socket.gethostname(),5000))
    serversocket2.listen(1)
    while True:
        clientsocket,adrr=serversocket2.accept()
        print "got connection from :",adrr
        clientsocket.send("confirmed TCP connection")
        data=clientsocket.recv(1024)
        print "Recived back from  TCP client",data
        clientsocket.close()


while True:
    try:
        rmesg,addr=serversocket.recvfrom(1024)
        if rmesg:
            rmesg=pickle.loads(rmesg)
            print rmesg[0],rmesg[3]
            if rmesg[0]==100 and rmesg[3]==101:
                serversocket.sendto("connection accepted", addr)
                print "sent connection accpted"
                TCPconnection()

            else:
                serversocket.sendto("connection refused", addr)

            serversocket.close()
            break
    except Exception as e:
        print ("wating for client to connect..Reason is :",e)
