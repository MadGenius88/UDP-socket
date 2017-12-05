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

