Nama  : Syarif Hidayatullah 
NIM   : 1203220094
Kelas : IF 02-01

PENJELASAN CARA KERJA PROGRAM PERMAINAN WARNA DENGAN PROTOKOL UDP

Sisi Server :
1. Inisialisasi Server : program dimulai dengan menginisialisasi server socket menggunakan 'socket.socket(socket.AF_INET, socket.SOCK_DGRAM)' untuk menggunakan protokol UDP.
2. Binding Soket : server mengikat soketnya ke alamat dan port yang ditentukan menggunakan 'server_socket.bind((server_ip, server_port))'.
3. Menerima dan Mengirim Pertanyaan : server akan masuk ke dalam loop untuk mengirim pertanyaan warna dalam bahasa Inggris kepada klien. setiap pertanyaan akan dikirim menggunakan 'server_socket.sendto()' dan dilakukan setiap 10 detik.
4. Penutupan Server : setelah semua pertanyaan telah dikirim, server menutup soketnya menggunakan 'server_socket.close()'.

Sisi Client :
1. Inisialisasi Client : program dimulai dengan menginisialisasi client socket menggunakan 'socket.socket(socket.AF_INET, socket.SOCK_DGRAM)' untuk menggunakan protokol UDP.
2. Binding socket : client mengikat soketnya ke alamat dan port yang telah ditentukan menggunakan 'client_socket.bind(("127.0.0.1", 54321))'.
3. Menerima Pertanyaan : client memasuki loop untuk menerima pertanyaan warna dalam bahasa Inggris dari server. setiap pertanyaan diterima menggunakan 'client_socket.recvfrom(1024)'.
4. Menjawab Pertanyaan : setelah menerima pertanyaan, client meminta pengguna memasukkan warna dalam bahasa Indonesia menggunakan 'input()'. setelah itu, client membandingkan jawaban pengguna dengan warna yang diterima dan memberikan nilai sesuai inputan pengguna.
5. Penutupan Client : setelah menjawab semua pertanyaan, client menutup soketnya menggunakan 'client_socket.close()'.

Cara Kerja Program :
1. Server akan dijalankan dan akan mulai mengirimkan pertanyaan warna kepada klien setiap 10 detik.
2. Setelah server aktif, satu atau lebih salinan dari sisi client dapat dijalankan. setiap salinan akan menunggu untuk menerima pertanyaan dari server.
3. Ketika pertanyaan diterima, setiap salinan sisi client akan meminta pengguna memasukkan warna dalam bahasa Indonesia dan memberikan nilai 100 apabila warna yang dijawab sesuai dan memberikan nilai 0 jika warna yang dijawab salah.
4. Proses ini berlanjut sampai server selesai mengirimkan pertanyaan atau dihentikan secara manual, dan setiap salinan dari sisi client telah menjawab semua pertanyaan dan ditutup.

.

.

.

SCREENSHOT 

Sisi Server 

![image](https://github.com/7Riv/Pemrograman-jaringan/assets/129931439/e62ce27e-a00f-4a17-bb10-311ec73275d9)

Client

![image](https://github.com/7Riv/Pemrograman-jaringan/assets/129931439/cdd09868-634a-476a-9692-ea35a5e7c39d)

Client2

![image](https://github.com/7Riv/Pemrograman-jaringan/assets/129931439/04f570ff-9b42-4761-a277-c5822f969fab)
