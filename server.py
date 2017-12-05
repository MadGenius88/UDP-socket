# Sender
import socket
import time

HOST = "localhost"
PORT = "5454"
data = "It always seems impossible until it's done - Nelson Mandela"

# Set up our sending socket UDP
class server
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind( (HOST,PORT) )
        
connections = []

# Send greeting to the receiver
def handler(c, a):
        while 2:
        s.sendto(data,(HOST<PORT))
        print "sent: "+data
        time.sleep(1)

