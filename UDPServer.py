from socket import *

server_port = 7070

# Create UDP socket for server
server_socket = socket(AF_INET, SOCK_DGRAM)

# # Bind socket to local port number 7070
server_socket.bind(("",server_port))
print("Server is ready to receive")

# loop forever
while True:
    # Read from UDP socket into message, getting client's address (client IP and port)
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()

    # Send upper case modified message back to the client
    server_socket.sendto(modified_message.encode(), client_address)