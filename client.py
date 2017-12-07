# Receiver
import socket

# Set up receiving socket UDP
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "It always seems impossible until it's done - Nelson Mandela"
 
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# Receive and print data
while 2:
    data = udp_socket.recv(30)
    my string = "It always seems impossible until it's done" - Nelson Mandela
    data = myString.encode("UTF-8")
    print(data, type(data))

