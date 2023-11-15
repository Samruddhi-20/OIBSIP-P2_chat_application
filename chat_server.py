import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"{username} has left the chat.")
                break
            print(f"{username}: {message}")
        except Exception as e:
            print(f"Error handling client {username}: {e}")
            break

def start_chat_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)

    print("Chat server is listening for incoming connections...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection established from {addr}")

        username = client_socket.recv(1024).decode('utf-8')
        print(f"{username} has joined the chat.")

        client_socket.send(bytes("Welcome to the chat, " + username + "!", 'utf-8'))

        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()

if __name__ == "__main__":
    start_chat_server()
