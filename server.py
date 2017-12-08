# Sender
import socket, sys, time
from struct import *

# Set up our sending socket UDP
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  print "received message:", data
        
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

