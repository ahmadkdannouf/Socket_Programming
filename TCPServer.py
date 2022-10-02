from socket import *

server_port = 7070

# Create TCP socket for server
server_socket = socket(AF_INET, SOCK_STREAM)

# # Bind socket to local port number 7070
server_socket.bind(("",server_port))
server_socket.listen(1)
print("Server is ready to receive")

# loop forever
while True:
    # Server waits on accept() from any requests from client, and a new socket is created on return
    connection_socket = server_socket.accept()

    # Read from newly established TCP connection socket into message
    message = connection_socket.recv(2048).decode()
    modified_message = message.decode().upper()

    # Send upper case modified message back to the client 
    connection_socket.send(modified_message.encode())

    # Close socket
    connection_socket.close()