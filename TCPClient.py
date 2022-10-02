from socket import * 

server_name = "127.0.0.1"
server_port = 7070

# Create TCP socket for client
client_socket = socket(AF_INET, SOCK_STREAM)

# Establish TCP connection to server
client_socket.connect((server_name, server_port))

# Get user input
message = input('Input lowercase sentence:')

# Send message into server socket
client_socket.send(message.encode())

# Client reads reply back from the server socket and converts it to string
# Notice we do not need to provide address information here. This is because 
#   the connection has already been established.
modified_message = client_socket.recv(2048)

# Client prints the modified message and closes the socket
print(modified_message.decode())
client_socket.close()