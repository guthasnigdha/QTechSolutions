import socket
import threading

# Function to receive messages from the server
def receive_messages(server_socket):
    while True:
        try:
            message = server_socket.recv(1024).decode("utf-8")
            if not message:
                print("Server disconnected.")
                break
            print("\nServer:", message)
        except:
            print("Connection lost.")
            break

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))  # Connect to server on localhost and port 12345
print("Connected to the server.")

# Start a thread to receive messages from the server
threading.Thread(target=receive_messages, args=(client,)).start()

# Sending messages to the server
while True:
    message = input("You: ")
    client.send(message.encode("utf-8"))
