import sys
import os
import json
import threading
from threading import current_thread
from multiprocessing.pool import ThreadPool
import subprocess
import socket_server as ss
import socket_client as sc

pool = ThreadPool(processes=2)
serverInstance = []

def start_server(socket_type, port):
    serverInstance.append(pool.apply_async(ss.Socket_Server, (socket_type, int(port))))
    print(socket_type+" listen on port "+port)

def get_hostname(socket_type,port):
    client = sc.Socket_Client(socket_type,int(port))
    if socket_type.upper() == "TCP":
        print(client.get_udp("hostname"))
    else:
        print(client.get_udp("hostname"))


def get_ip_server(socket_type,port):
    client = sc.Socket_Client(socket_type, int(port))
    if socket_type.upper() =="UDP":
        print(client.get_udp("server-ip"))
    else:
        print(client.get_udp("server-ip"))

def get_running_process(socket_type):
    print("")

def upload_file(filename,socket_type,port):
    client = sc.Socket_Client(socket_type, int(port))
    if socket_type.upper() == "UDP":
        print(client.get_udp("list-messages"))
    else:
        client.send_file_udp("upload",filename)

def list_files(socket_type,port):
    client = sc.Socket_Client(socket_type, int(port))
    if socket_type.upper() == "UDP":
        print(client.get_udp("list-messages sent"))
    else:
        print(client.get_udp("list-messages sent"))

def get_time(country,socket_type,port):
    client = sc.Socket_Client(socket_type, int(port))
    if socket_type.upper() == "UDP":
        print(client.get_udp("elapsed time "+message)
    else:
        print(client.get_udp("num time "+message))

avaiable_commands = {
        'start server': start_server,
        'get hostname': get_hostname,
        'get server-ip': get_ip_server,
        'get runing-process': get_running_process,
        'upload file': upload_file,
        'list messages': list_messages,
        'get elapsed time': get_elapsed_time
}


def main():
    show_menu()
    main_control()

def show_menu():
    cls()
    print("Avaiable commands, (1. and 7. include params)")
    print("1. start server (UDP) port")           #2
    print("2. get hostname (UDP) port")           #2
    print("3. get server-ip (UDP) port")          #2
    print("4. get running-process time received (UDP) port")     #2
    print("5. upload packet filename (UDP) port")   #3
    print("6. list messages (UDP) port")             #2
    print("7. get elapsed time message sent (UDP) port")       #3

def main_control():
    print("Enter a command")
    while True:
        input_var = input(">")
        for x in avaiable_commands:
            command = input_var.rsplit(None, 5)[:2]
            newc = " ".join(str(x) for x in command)
            if x == newc:
                if (newc == "upload file") or (newc == "get time"):
                    try:
                        if len(input_var.split(" ")) == 6:
                            param1 = input_var.split(' ', 5)[2:4]
                            param1 = " ".join(str(x) for x in param1)
                        else:
                            param1 = input_var.split(' ', 5)[2]
                        param2 = input_var.split(' ', 5)[-2]
                        param3 = input_var.split(' ', 5)[-1]
                        avaiable_commands[newc](param1, param2,param3)
                    except IndexError:
                        continue
                else:
                    try:
                        param1 = input_var.split(' ', 4)[2]
                        param2 = input_var.split(' ', 4)[3]
                        avaiable_commands[newc](param1, param2)
                    except IndexError:
                        continue

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')



main()
