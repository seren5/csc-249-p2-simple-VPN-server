#!/usr/bin/env python3

import socket
import arguments
import argparse

# Run 'python3 VPN.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and prints the response')
parser.add_argument('--VPN_IP', help='IP address at which to host the VPN', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which to host the VPN', **arguments.vpn_port_arg)
args = parser.parse_args()

VPN_IP = args.VPN_IP  # Address to listen on
VPN_PORT = args.VPN_port  # Port to listen on (non-privileged ports are > 1023)

def parse_message(message):
    message = message.decode("utf-8")
    # Parse the application-layer header into the destination SERVER_IP, destination SERVER_PORT,
    # and message to forward to that destination
    SERVER_IP, SERVER_PORT, equation = message.split('|')
    # raise NotImplementedError("Your job is to fill this function in. Remove this line when you're done.")
    return SERVER_IP, int(SERVER_PORT), equation

### INSTRUCTIONS ###
# The VPN, like the server, must listen for connections from the client on IP address
# VPN_IP and port VPN_port. Then, once a connection is established and a message recieved,
# the VPN must parse the message to obtain the server IP address and port, and, without
# disconnecting from the client, establish a connection with the server the same way the
# client does, send the message from the client to the server, and wait for a reply.
# Upon receiving a reply from the server, it must forward the reply along its connection
# to the client. Then the VPN is free to close both connections and exit.

# The VPN server must additionally print appropriate trace messages and send back to the
# client appropriate error messages.
print("vpn starting - listening for connections at IP", VPN_IP, "and port", VPN_PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as vpn_s:
    VPN_PORT = int(VPN_PORT)
    vpn_s.bind((VPN_IP, VPN_PORT))
    vpn_s.listen()
    client_conn, client_addr = vpn_s.accept()
    with client_conn:
        print(f"Connected established from {client_addr}")
        while True:
            data = client_conn.recv(1024) # Receives data from the client
            if not data:
                print("no data received from client") 
                client_conn.sendall(b"Error: No data received.")
                break # Breaks after receiving no data from client

            server_ip, server_port, equation = parse_message(data)
            print("forwarding message to server")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_s:
                try:
                    server_s.connect((server_ip, server_port))
                    print(f"connection established with server, sending message")
                    
                    server_s.sendall(bytes(equation, "utf-8"))
                    print("message sent, waiting for reply")
                    
                    server_response = server_s.recv(1024).decode("utf-8")
                    print(f"Received response: '{server_response} [{len(server_response)} bytes]")

                    if server_response:
                        print("sending result to client")
                        client_conn.sendall(bytes(server_response, "utf-8"))

                    else:
                        print("received empty reponse from server")
                        client_conn.sendall(b"Error: Received empty response from server.")

                except Exception as e:
                    print(f"Error connecting to server: {e}")
                    client_conn.sendall(b"Error: Could not connect to server.")
