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

# Send packet to the receiver
def handler(c, a):
        while 2:
        s.sendto(data,(HOST<PORT))
        print "sent: "+data
        time.sleep(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind('127.0.0.1',5005)

while 1:
    packet = sock.recvfrom(65565)
    packet = packet[0]

    # parse IP
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)

    #all the following values are incorrect
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF

    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);

    # parse UDP
    packet = packet[20:28]
    data = packet[header_length:]
    source_port, dest_port, data_length, checksum = struct.unpack("!HHHH", header)


