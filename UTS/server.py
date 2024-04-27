import socket
import random
import time

def generate_random_color():
    colors = ['red', 'purple', 'black', 'white', 'green', 'blue']
    return random.choice(colors)

def main():
    server_ip = "127.0.0.1"
    server_port = 12345
    num_questions = 10

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print("Server is running...")

    for _ in range(num_questions):
        color = generate_random_color()
        print(f"Sending color: {color}")
        server_socket.sendto(color.encode(), ("127.0.0.1", 54321))
        time.sleep(10)

    server_socket.close()
    print("Server has finished sending questions.")

if __name__ == "__main__":
    main()
