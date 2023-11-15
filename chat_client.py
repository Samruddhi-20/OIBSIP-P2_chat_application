import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_chat_client():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 2000))
    server.listen(5)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 2000))


    username = input("Enter your username: ")
    client.send(bytes(username, 'utf-8'))

    welcome_message = client.recv(1024).decode('utf-8')
    print(welcome_message)

    message_receiver = threading.Thread(target=receive_messages, args=(client,))
    message_receiver.start()

    while True:
        message = input()
        client.send(bytes(message, 'utf-8'))

if __name__ == "__main__":
    start_chat_client()
