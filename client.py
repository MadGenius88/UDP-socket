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
    my string = "It always seems impossible until it's done" - Nelson Mandela
    data = myString.encode("UTF-8")
    print(data, type(data))

