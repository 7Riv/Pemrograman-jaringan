import socket
import random
import threading
import time

def generate_random_color():
    colors = ['red', 'purple', 'white', 'blue', 'green', 'black']
    return random.choice(colors)

def handle_client(client_socket, client_address):
    num_questions = 10
    for _ in range(num_questions):
        color = generate_random_color()
        print(f"Sending color {color} to {client_address}")
        client_socket.send(color.encode())
        time.sleep(10)
    print(f"Finished sending questions to {client_address}")
    client_socket.close()

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print("Server is running...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        time.sleep(1)  

if __name__ == "__main__":
    main()
