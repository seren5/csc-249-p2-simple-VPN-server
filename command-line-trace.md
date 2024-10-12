# Command Line Trace Basic Math Server
basic math server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 51999)
Received client message: 'b'+1:3:5'' [6 bytes]
requested operation is addition
request includes 3 arguments: 1 3 5
result of operation: 9
sending result message 1+3+5=9
server is done!

# Command Line Trace VPN (with Basic Math Server)
vpn starting - listening for connections at IP 127.0.0.1 and port 55554
Connected established from ('127.0.0.1', 51998)
forwarding message to server
connection established with server, sending message
message sent, waiting for reply
Received response: '1+3+5=9 [7 bytes]
sending result to client
vpn is done!

# Command Line Trace Client (with Basic Math Server)
client starting - connecting to VPN at IP 127.0.0.1 and port 55554
would you like to connect to basic math or other? (1 for basic math, 2 for other, 3 to exit) [disclaimer: you can only connect to the server you run]    1
What (addition/subtraction) equation would you like solved? (Please enter your equation in the following format: +1:3:5 or -1:3:5. The order of the numbers matter.)   +1:3:5
connection established, sending message '127.0.0.1|65432|+1:3:5'
message sent, waiting for reply
Received response: '1+3+5=9' [7 bytes]
client is done!




# Command Line Trace Echo Server
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 52420)
Received client message: 'b'Hello, world'' [12 bytes]
echoing 'b'Hello, world'' back to client
server is done!

# Command Line Trace VPN (with Echo Server)
vpn starting - listening for connections at IP 127.0.0.1 and port 55554
Connected established from ('127.0.0.1', 52419)
forwarding message to server
connection established with server, sending message
message sent, waiting for reply
Received response: 'Hello, world [12 bytes]
sending result to client
vpn is done!

# Command Line Trace Client (with Echo Server)
client starting - connecting to VPN at IP 127.0.0.1 and port 55554
would you like to connect to basic math or other? (1 for basic math, 2 for other, 3 to exit) [disclaimer: you can only connect to the server you run]    2
connection established, sending message '127.0.0.1|65432|Hello, world'
message sent, waiting for reply
Received response: 'Hello, world' [12 bytes]
client is done!