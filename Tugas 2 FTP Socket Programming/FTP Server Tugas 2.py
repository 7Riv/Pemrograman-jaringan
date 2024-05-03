import socket
import os

SERVER_ADDRESS = ("localhost", 5002)
BUFFER_SIZE = 4096

def list_files(server_directory):
    files = os.listdir(server_directory)
    return "\n".join(files)

def delete_file(server_directory, filename):
    path = os.path.join(server_directory, filename)
    try:
        os.remove(path)
        return f"File {filename} berhasil dihapus."
    except FileNotFoundError:
        return "File tidak ditemukan."

def get_file_size(server_directory, filename):
    try:
        path = os.path.join(server_directory, filename)
        filesize = os.path.getsize(path)
        return f"Size: {filesize / 1024:.2f} KB"
    except FileNotFoundError:
        return "File tidak ditemukan."

def handle_command(conn, command, server_directory):
    response = None
    if command.lower().startswith("ls"):
        response = list_files(server_directory)
    elif command.startswith("rm"):
        _, filename = command.split(maxsplit=1)
        response = delete_file(server_directory, filename)
    elif command.startswith("size"):
        _, filename = command.split(maxsplit=1)
        response = get_file_size(server_directory, filename)
    elif command.startswith("download"):
        _, filename = command.split(maxsplit=1)
        file_path = os.path.join(server_directory, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, "rb") as f:
                    file_data = f.read()
                    file_length = len(file_data)
                    conn.sendall(file_length.to_bytes(4, byteorder='big'))
                    conn.sendall(file_data)
            except Exception as e:
                print(f"Gagal menerima file: {str(e)}")
        else:
            print("File tidak ditemukan pada server.")
    elif command == "connme":
        response = "[+] Berhasil Terkoneksi."
    else:
        response = "Perintah tidak valid."
    
    if response:
        conn.send(response.encode())


def main():
    server_directory = input("Masukkan direktori server: ").strip()

    if not os.path.exists(server_directory):
        print("Direktori server tidak ditemukan.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(SERVER_ADDRESS)
        s.listen()
        print("[*] Menunggu Koneksi")
        conn, addr = s.accept()
        print("[+] Berhasil Terkoneksi.")
        with conn:
            while True:
                command = conn.recv(BUFFER_SIZE).decode()
                if not command:
                    break
                print(f"Menerima perintah: {command}")
                if command.lower() == "byebye":
                    conn.send("Koneksi terputus dengan server.".encode())
                    break
                handle_command(conn, command, server_directory)
        conn.close()

if __name__ == "__main__":
    main()
