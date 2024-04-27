import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    num_questions = 10
    for _ in range(num_questions):
        received_color = client_socket.recv(1024).decode()
        print(f"Received color: {received_color}")

        user_response = input("Masukkan warna dalam bahasa Indonesia: ").lower()

        if user_response == "merah" and received_color == "red":
            print("Jawaban benar! Nilai: 100")
        elif user_response == "ungu" and received_color == "purple":
            print("Jawaban benar! Nilai: 100")
        elif user_response == "putih" and received_color == "white":
            print("Jawaban benar! Nilai: 100")
        elif user_response == "biru" and received_color == "blue":
            print("Jawaban benar! Nilai: 100")
        elif user_response == "hijau" and received_color == "green":
            print("Jawaban benar! Nilai: 100")
        elif user_response == "hitam" and received_color == "black":
            print("Jawaban benar! Nilai: 100")
        else:
            print("Jawaban salah. Nilai: 0")

    client_socket.close()

if __name__ == "__main__":
    main()
