import socket
import random
import time
import threading

def generate_random_color():
    colors = ['red', 'purple', 'white', 'blue', 'green', 'black']
    return random.choice(colors)

def handle_client(server_socket, client_address):
    num_questions = 10
    for _ in range(num_questions):
        color = generate_random_color()
        print(f"Sending color {color} to {client_address}")
        server_socket.sendto(color.encode(), client_address)
        time.sleep(10)
    print(f"Finished sending questions to {client_address}")

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print("Server is running...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(server_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
