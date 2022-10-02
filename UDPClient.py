from socket import * 

server_name = "127.0.0.1"
server_port = 7070

# Create UDP socket for client
client_socket = socket(AF_INET, SOCK_DGRAM)
another_socket = socket(AF_INET, SOCK_DGRAM)

# Get user input
message = input('Input lowercase sentence:')
another_message = "hi jeff"

# Send message into server socket
client_socket.sendto(message.encode(), (server_name, server_port))
another_socket.sendto(another_message.encode(), (server_name, server_port))

# Client reads reply back from the server socket and converts it to string
# This recvfrom method returns the message and the IP address of the sender of the message
modified_message, server_address = client_socket.recvfrom(2048)
another_modified_message, server_address = another_socket.recvfrom(2048)

# Client prints the modified message and closes the socket
print(modified_message.decode())
print(another_modified_message.decode())
client_socket.close()
another_socket.close()