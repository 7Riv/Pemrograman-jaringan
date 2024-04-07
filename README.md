Nama : Syarif Hidayatullah
NIM : 1203220094

PENJELASAN KODE PROGRAM

Kode Server (FTP Server Tugas2.py):

1. Impor Modul: Pertama-tama, modul socket dan os diimpor untuk mengaktifkan fungsi-fungsi yang diperlukan.
2. Penetapan Variabel: Variabel seperti SERVER_ADDRESS dan BUFFER_SIZE ditetapkan untuk menentukan alamat server dan ukuran buffer untuk menerima data.
3. Membuat Direktori Server: Jika tidak ada, skrip akan membuat direktori 'server' di mana file-file akan disimpan.
4. Fungsi-fungsi: Ada beberapa fungsi yang didefinisikan:
      - list_files(): Mengembalikan daftar file dan folder di direktori server.
      - remove_file(filename): Menghapus file dengan nama tertentu dari direktori server.
      - download_file(filename): Mengirimkan isi file dengan nama tertentu dari direktori server.
      - upload_file(filename, data): Menerima dan menyimpan file dengan nama tertentu di direktori server.
      - get_file_size(filename): Mengembalikan ukuran file dalam megabytes (MB) dari file dengan nama tertentu.
5. Fungsi handle_client(conn): Fungsi ini menangani setiap koneksi client-server. Ia menerima perintah dari client, menjalankan fungsi yang sesuai, dan mengirimkan respons kembali kepada client.
6. Pengikatan dan Pendengaran: Server membuat socket, mengikatnya ke alamat yang ditentukan, dan mulai mendengarkan koneksi dari client. Setelah koneksi diterima, server mulai menangani client dengan memanggil fungsi handle_client(conn).

Kode Client (FTP Client Tugas 2.py):

1. Impor Modul: Modul socket dan os diimpor untuk mendukung fungsionalitas client.
2. Penetapan Variabel: Variabel seperti SERVER_ADDRESS dan BUFFER_SIZE ditetapkan untuk menentukan alamat server dan ukuran buffer untuk menerima data.
3. Membuat Direktori Client: Jika tidak ada, skrip akan membuat direktori 'client' di mana file-file akan disimpan.
4. Fungsi-fungsi: Ada dua fungsi yang didefinisikan:
      - receive_file(s, filename): Menerima file dari server dan menyimpannya di direktori client.
      - sent_file(conn, filename): Mengirimkan file dari client ke server.
5. Menghubungkan ke Server: Client mencoba untuk terhubung ke server. Jika berhasil, client dapat mulai mengirimkan perintah.
6. Loop Utama: Client memasukkan perintah dari pengguna dan mengirimkannya ke server. Client juga menerima respons dari server dan menangani pengunduhan atau pengiriman file sesuai kebutuhan.


CARA MENGGUNAKAN COMMAND DARI SERVER DAN CLIENT:

Server:
1. Jalankan Server: Jalankan skrip server.py di terminal atau lingkungan Python.
2. Tunggu Koneksi: Server akan menunggu koneksi dari client.
3. Terima Perintah: Setelah koneksi berhasil, server akan menerima perintah dari client.
4. Tanggapi Perintah: Server akan menanggapi perintah yang diterima sesuai dengan implementasinya.
5. Putuskan Koneksi: Jika client mengirim perintah 'byebye', server akan menutup koneksi dengan client.

Client:
1. Jalankan Client: Jalankan skrip client.py di terminal atau lingkungan Python.
2. Masukkan Perintah: Client akan meminta Anda untuk memasukkan perintah.
3. Kirim Perintah ke Server: Masukkan perintah yang diinginkan dan kirim ke server.
4. Terima Respons: Client akan menerima respons dari server berdasarkan perintah yang dikirimkan.
5. Lanjutkan Interaksi: Anda dapat terus berinteraksi dengan client dan mengirimkan perintah baru ke server.
