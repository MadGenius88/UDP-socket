import socket
import sys
import select
import os
from geopy import geocoders
from datetime import datetime
import pytz

class Socket_Server:

    def __init__(self,type,port):

        self.server_address = (socket.gethostname(), port)
        self.server_ip = socket.gethostbyname(socket.getfqdn())
        self.unknown_command_error = "Unknown command"

        if type.upper() == "UDP":
            # Create UDP socket
            self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
            self.sock.bind(self.server_address)
            self.manage_conections_udp()

    def list_files(self):
        dirs = os.listdir(os.path.dirname(os.path.abspath(__file__)))
        files = " ".join(str(x) for x in dirs)
        return files

    def get_time(self,country):
        g = geocoders.GoogleV3()
        place, (lat, lng) = g.geocode(country)
        timezone = g.timezone((lat, lng))  # return pytz timezone object
        now = datetime.now(pytz.timezone(timezone.zone))
        return now.ctime()

    def get_command_and_param(self,data):
        param = data.decode().rsplit(None, 2)[1:]
        param = " ".join(str(x) for x in param)
        data = data.decode().rsplit(None, 2)[0]
        return (data,param)

    def manage_conections_udp(self):
        while True:
            data, address = self.sock.recvfrom(1024)
            data,param = self.get_command_and_param(data)
            if data == "hostname":
                self.sock.sendto(socket.gethostname().encode(encoding='utf_8'), address)
            elif data == "server-ip":
                self.sock.sendto(self.server_ip.encode(encoding='utf_8'), address)
            elif data == "list-files":
                self.sock.sendto(self.list_files().encode(encoding='utf_8'), address)
            elif data == "time":
                self.sock.sendto(self.get_time(param).encode(encoding='utf_8'), address)
            elif data == "upload":
                self.sock.sendto(self.get_time(param).encode(encoding='utf_8'), address)
                print("goit")
                # data, addr = self.sock.recvfrom(1024)
                # f = open(data.decode(), 'wb')
                #
                # data, addr = self.sock.recvfrom(1024)
                # print("goit3")
                # try:
                #     while (data):
                #         f.write(data)
                #         self.sock.settimeout(2)
                #         data, addr = self.sock.recvfrom(1024)
                #     print("File Downloaded")
                # except socket.timeout:
                #     f.close()
                #     self.sock.close()
                #     print("File Downloaded")


    def manage_conections_tcp(self):

        while True:
            # Wait for a connection
            #print ('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                #print ('connection from', client_address)

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(1024)
                    data, param = self.get_command_and_param(data)
                    if data == "hostname":
                        connection.sendall(socket.gethostname().encode(encoding='utf_8'))
                    elif data == "server-ip":
                        connection.sendall(self.server_ip.encode(encoding='utf_8'))
                    elif data == "list-files":
                        connection.sendall(self.list_files().encode(encoding='utf_8'))
                    elif data == "time":
                        connection.sendall(self.get_time(param).encode(encoding='utf_8'))
                    else:
                        connection.sendall(self.unknown_command_error.encode(encoding='utf_8'))
                        break

            finally:
                # Clean up the connection
                connection.close()


#newSoc = Socket_Server("TCP",6868);
