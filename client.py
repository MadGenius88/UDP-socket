# Receiver
import socket, sys, time
from struct import *

# Set up receiving socket UDP
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "It always seems impossible until it's done - Nelson Mandela"
MAX_FAILS_SENDING = 10
MTU_DISCOVERY_SEQ = 0 # the Sequence number sending MTU discovery messages
TIMEOUT = 0.0005
BUFFER  = 64536
 
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

# Checksum functions needed for calculation checksum
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def test_adler32start(self):
        self.assertEqual(zlib.adler32(""), zlib.adler32("", 1))
        self.assert_(zlib.adler32("abc", 0xffffffff))

def checksum = sum(bytearray(b)"UTF-4")

# Receive and print data
while 2:
    data = udp_socket.recv(30)
    my string = "It always seems impossible until it's done" - Nelson Mandela
    data = myString.encode("UTF-8")
    print(data, type(data))

# Payload size
with open('payloadfile.bin') as op:
    payload = pickle.load(op)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in payload:
    sock.sentto(payload, ('127.0.0.1',5005))

