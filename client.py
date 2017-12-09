# Receiver
import socket, sys, time
from struct threading *

# Set up receiving socket UDP
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MAX_FAILS_SENDING = 10
MTU_DISCOVERY_SEQ = 0 # the Sequence number sending MTU discovery messages
TIMEOUT = 0.0002
BUFFER  = 64536
 
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

# Elaspsed time 
   for pings in range(10):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    message = 'test'
    addr = ("127.0.0.1", 12000)

    start = time.time()
    clientSocket.sendto(message, addr)
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print '%s %d %d' % (data, pings, elapsed)
    except timeout:
        print 'REQUEST TIMED OUT'

# Checksum functions needed for calculation checksum
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(bytes(MESSAGE), (UDP_IP, UDP_PORT))

def adler32start(self):
        self.assertEqual(zlib.adler32(""), zlib.adler32("", 1))
        self.assert_(zlib.adler32("abc", 0xffffffff))

def checksum = sum(bytearray(b)"UTF-4")
    sock.sendto(bytes(MESSAGE, "UTF-4"), (UDP_IP, UDP_PORT))

# Receive and print data
while 2:
    data = udp_socket.recv(30)
    my string = "It always seems impossible until it's done" - Nelson Mandela
    data = myString.encode("UTF-8")
    print(data, type(data))

# Payload size
with open('payloadfile.bin') as op:
    payload = pickle.load(op)
  
def payload = sum(bytearray(b)"UTF-2")
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
     sock.sendto(bytes(MESSAGE, "UTF-8"), (UDP_IP, UDP_PORT))

for i in payload:
    sock.sentto(payload, ('127.0.0.1',5005))
    print(data, type(data))

