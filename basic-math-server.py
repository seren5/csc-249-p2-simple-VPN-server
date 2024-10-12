#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def rearrange_equation(data):
    if data.startswith('+'): # Checks if data starts with + or -
        data = data[1:] # Removes the - as it starts from position 1
        numbers = data.split(':') # Takes out the ":"
        data = '+'.join(numbers) # Puts + in between
        return data
    elif data.startswith('-'): # See line 9
        data = data[1:] # Removes the - as it starts from position 1
        numbers = data.split(':') # Takes out the ":"
        data = '-'.join(numbers) # Puts - in between
        return data
    else:
        print("error! please try again later ^-^") # This won't happen because the the client side makes sure of that, but I added it anyways

def addition_or_subtraction(data):
    if "+" in data: # Sees if the operation is addition
        print("requested operation is addition")
    elif "-" in data:
        print("requested operation is subtraction") # Sees if the operation is subtraction

def extract_arguments(data):
    data = data[1:] # Removes the + or - symbol since client checked position of "+" and "-"
    data_bits = data.split(':') # Removes the ":"
    numeric_bits = [part for part in data_bits if part.isdigit()] # Takes only the numbers from data_bits
    arguments = ' '.join(numeric_bits) # Puts a space between the numbers
    return arguments

def num_of_arguments(data):
    return sum(char.isdigit() for char in data) # Returns the sum/total of digits in data

def evaluate_expression(equation): # Evaluates the sum (or difference) of the equation
    result = eval(equation)
    result = str(result) # Turns result into str because print can't concatenate a string and an integer
    print("result of operation: " + result)
    return result


print("basic math server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024) # 1024 => number of bytes
            if not data:
                break
            data.decode('utf-8') # to remove the 'b' in front of the print
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            data = data.decode('utf-8') # decodes and saves data as decoded so the methods can use it
            addition_or_subtraction(data) # checks whether it's addition or subtraction
            number = num_of_arguments(data) # gives number of arguments
            print('request includes ', end = "") # Had weird bugs with printing so I added this, gives number of arguments and arguments,
            print(number, end="")
            print(' arguments: ', end = "")
            print(extract_arguments(data))
            
            equation = rearrange_equation(data) # Rearranges data to the form of e.g. 1+3+5 instead of +1:3:5
            result = evaluate_expression(equation) # Result is the sum or difference of the equation
            
            full_equation = equation + "=" + result # Creates the format a+b+c " = " x
            print("sending result message " + full_equation)
            data = full_equation # Updates data to send back
            conn.sendall(data.encode('utf-8')) # Sends data back to the client
            print("server is done!")



