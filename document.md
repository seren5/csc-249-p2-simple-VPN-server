
# Client-VPN Message Format Document

This document is a written description of my client-VPN message format.


# Overview of Application

This applications utilizes a client, VPN, and server to send messages. The client sends an encoded message (with the server IP and port) to the VPN, which decodes it, encodes it once more to send to the server, and the server receives the message. Then, depending on the function of the server, it may echo the message back the same way it came (the server does not need to know the IP address nor port of the client, as the VPN has it already), or process basic functions depending on what server it is.


# Client -> VPN Server Message Format

The message from the client to the VPN server is shown in the format of SERVER_IP|SERVER_PORT|message, so that the client may send the message to the VPN server at SERVER_IP and SERVER_PORT.
The message is either a string that the echo server may echo, or a basic math equation that links up to my previous project, a basic math server.


# VPN Server -> Client Message Format

The message from the VPN server to the client is just forwarded from the server to the client after decoding then encoding once more.


# Example Output

This can be seen in the command-line-trace with 2 examples of it working with the echo server and the basic math server.


# Description of how the network layers interact

First, the client creates a TCP connection using the VPN's server IP and port and sends an encoded message. (The client can be considered as the application layer)
Next, the VPN listens for connections, then parses the message received from the client.
Then, the VPN also creates a TCP connection with the server using the final server's IP and port, and forwards the message.
The final server decodes the message, processes it, then sends it to the VPN, which forwards it back to the client.

The TCP layers for the client and VPN make sure that the message is delivered reliably.


# Acknowledgments

Isabelle helped me understand the encoding and decoding between servers.
https://www.w3schools.com/python/ref_string_split.asp (My split was having issues that confused me)