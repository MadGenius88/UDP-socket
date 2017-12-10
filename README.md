# Python UDP-socket
Simple UDP server/client socket communication

[![UDP Communication][3]][4] 

## Introduction

Sockets are fundamentals. It's behind any kind of network communication done by the computers. It's the backbone behind world wide web. For example when you type "www.google.com" in your web browser, it will open a socket and connect to google.com to get a web page and show it to you in HTML format. Similar to chat client like google hangout, yahoo messenger or skype.

To begin our project to the socket world, we will do programming udp socket in python. To start, let's begin with creating a socket

## Create a Socket Example

To create a socket, we can use python's [socket](https://docs.python.org/2/library/socket.html). Now let's create one:

    # Code 1.py
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socked created!")

The code was straight forward. We first import `socket` library. Then we create a socket using `socket.socket` function. We passed `AF_INET` as IPv4 as the address family like '127.0.0.1' and `SOCK_DGRAM` means we used UDP protocol.

## Connect To The Server Example

After creating a socket, we now able to connect to the server via a certain port number. We need an IP address and port number to connect to. We will use port 80 which is http default port and ip address of google.com as an example.

### Get IP Address From The Host Example

It's simple. We can use `gethostbyname` function to get IP address from hostname.

## UDP Client/Server Project Outline

### Create a UDP client & server: 
    It should have a command line flag that specifies the port and another flag to specify what host:
    port it should connect and send data to
    This can be one application, that can act as either server/client, or two separate applications
    Send one IPv4 UDP packet every two seconds with a payload of data
    In the payload, byte encode the string `"It always seems impossible until it's done" - Nelson Mandela` 
    along with a timestamp and the IPv4 address and port the sender is listening on
    
### The payload of data should not exceed the default UDP MTU size (64k) and should be structured like this:
    checksum (Adler32) - 4 bytes
    unix timestamp - 8 bytes
    ipv4 - 4 bytes
    port - 2 bytes
    Nelson Mandela quote
    When the packet is received
    Print the quote
    Print the time elapsed since the message was sent
    Print the source IPv4 address
    Print how many times that source IP sent a message
