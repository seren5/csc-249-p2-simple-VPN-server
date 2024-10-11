#!/usr/bin/env python3

import socket
import arguments
import argparse

# Run 'python3 client.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and print the response')
parser.add_argument('--server_IP', help='IP address at which the server is hosted', **arguments.ip_addr_arg)
parser.add_argument('--server_port', help='Port number at which the server is hosted', **arguments.server_port_arg)
parser.add_argument('--VPN_IP', help='IP address at which the VPN is hosted', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which the VPN is hosted', **arguments.vpn_port_arg)
parser.add_argument('--message', default=['Hello, world'], nargs='+', help='The message to send to the server', metavar='MESSAGE')
args = parser.parse_args()

SERVER_IP = args.server_IP  # The server's IP address
SERVER_PORT = args.server_port  # The port used by the server
VPN_IP = args.VPN_IP  # The server's IP address
VPN_PORT = args.VPN_port  # The port used by the server
MSG = ' '.join(args.message) # The message to send to the server

def encode_message(message):
    # Add an application-layer header to the message that the VPN can use to forward it
    return f"{SERVER_IP}|{SERVER_PORT}|{message}" # Combines server information with the message


print("client starting - connecting to VPN at IP", VPN_IP, "and port", VPN_PORT)

exit_loop = False
while exit_loop == False:
    connection_choice = input("would you like to connect to basic math or other? (1 for basic math, 2 for other)    ")
    if connection_choice == "1":
        exit_loop_2 = False
        while exit_loop_2 == False:
            msg = input("What (addition/subtraction) equation would you like solved? (Please enter your equation in the following format: +1:3:5 or -1:3:5. The order of the numbers matter.)   ") # Asks for user input
            if msg == "quit": # If the user inputs quit, the program exits
                print("client quitting at operator request")
                exit(0)
            elif msg == "": # If the user inputs an empty message, they are prompted to put in numbers again
                print("You have not specified a value, please try again.")
            elif msg.startswith("+") or msg.startswith("-"):
                if ":" in msg and "0" in msg or "1" in msg or "2" in msg or "3" in msg or "4" in msg or "5" in msg or "6" in msg or "7" in msg or "8" in msg or "9" in msg: # Checks for ":" or number (it isn't the prettiest but I couldn't get it to work in time)
                    break
                else: # The user has input a letter or did not start with "+" or "-"
                        print("Please format your equation in the following format:+1:3:5 or -1:3:5")
            else: # The user has input a letter or did not start with "+" or "-"
                    print("You have not formatted your equation properly.")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((VPN_IP, VPN_PORT))
            print(f"connection established, sending message '{encode_message(msg)}'")
            MSG = encode_message(MSG)
            s.sendall(bytes(MSG, 'utf-8'))
            print("message sent, waiting for reply")
            data = s.recv(1024).decode("utf-8")
    elif connection_choice == "2":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((VPN_IP, VPN_PORT))
            print(f"connection established, sending message '{encode_message(MSG)}'")
            MSG = encode_message(MSG)
            s.sendall(bytes(MSG, 'utf-8'))
            print("message sent, waiting for reply")
            data = s.recv(1024).decode("utf-8")
            break
    else:
        print("you have not selected a choice. please try again.")
     
    
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((VPN_IP, VPN_PORT))
#     print(f"connection established, sending message '{encode_message(MSG)}'")
#     MSG = encode_message(MSG)
#     s.sendall(bytes(MSG, 'utf-8'))
#     print("message sent, waiting for reply")
#     data = s.recv(1024).decode("utf-8")

print(f"Received response: '{data}' [{len(data)} bytes]")
print("client is done!")
