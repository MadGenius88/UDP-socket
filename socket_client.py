import socket
import sys


class Socket_Client:

    def __init__(self,type, port):
        self.server_address = (socket.gethostname(), port)
        if type.upper() == "UDP":
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.connect(self.server_address)

    def get_udp(self,message):
        self.sock.sendto(message.encode(encoding='utf_8'),self.server_address)
        data, address = self.sock.recvfrom(1024)
        self.sock.close()
        return data.decode()

    def get_udp(self,message):
        self.sock.sendall(message.encode(encoding='utf_8'))
        response = self.sock.recv(1024).decode()
        self.sock.close()
        return response

    def send_filename_udp(self,message,filename):
        self.sock.sendto(message.encode(encoding='utf_8'), self.server_address)
        data, address = self.sock.recvfrom(1024)
        print(data)
        # buf = 1024
        # self.sock.sendto(filename.encode(encoding='utf_8'), self.server_address)
        # f = open(filename, "rb")
        # data = f.read(buf)
        # while (data):
        #     if (self.sock.sendto(data, self.server_address)):
        #         data = f.read(buf)
        # self.sock.close()
        # f.close()

    def manage_client_requests(self):
        try:
            # Send data
            message = 'It always seems impossible until it's done" - Nelson Mandela'
            print('sending "%s"' % message)
            self.sock.sendall(message.encode(encoding='utf_8'))

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received "%s"' % data)

        finally:
            print('closing socket')
            self.sock.close()

#newClient = Socket_Client('127.0.0.1',6868,"UDP")
