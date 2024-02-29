import socket
i = 1
# Define the host and port on which the server will listen
host = socket.gethostbyname(socket.gethostname())  # localhost
port = 12345        # arbitrary port number

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server.bind((host, port))

# Listen for incoming connections
server.listen(5)  # queue up to 5 connections

print(f"[*] Listening on {host}:{port}")

# Accept incoming connection
client_socket, client_address = server.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
while True: 
    commands = input("Enter command to send: ")
    # Send the command to the client
    client_socket.send(commands.encode())
    # Receive the output from the client
    response = client_socket.recv(4096)
    print(f"[*] Received from client for command '{commands}':")
    print(response.decode())

