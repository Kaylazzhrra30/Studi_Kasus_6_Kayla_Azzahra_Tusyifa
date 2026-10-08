# Studi_Kasus_6_Kayla_Azzahra_Tusyifa

NAMA  : Kayla Azzahra Tusyifa

NIM   : 2609116027 (Ganjil)

KELAS : A 2026

*SISTEM PENCATATAN NILAI UJIAN MAHASISWA*

*1. PENJELASAN SINGKAT KODE DAN FUNGSINYA*

Saya memilih menggunakan *CSV (Comma Separated Value)* yaitu sebuah file teks sederhana untuk menyimpan data mahasiswa yang berisi nama, nim, matkul dan nilai dalam format tabel dimana nilai dipisahkan dengan koma dan baris data dipisahkan dengan garis baru 
<img width="1460" height="637" alt="402CA60F-714A-43D9-ABC3-07855C9563DA_1_201_a" src="https://github.com/user-attachments/assets/4bfb7cad-bfa6-4f15-aeb7-56ba72a71369" />

Pada program kali ini saya juga menggunakan *import csv* untuk menambah fitur CSV pada program/file python, kemudian *while True* digunakan untuk perulangan agar program berjalan  terus sampai user memilih opsi keluar, *input* untuk memasukkan pilihan menu dan data mahasiswa, *print* untuk menampilkan output teks yang kita inginkan, lalu *if* adalah suatu kondisi untuk menentukan perintah yang dijalankan sesuai kondisi, dan pada program kali ini digunakan untuk memeriksa pilihan menu yang dimasukkan user.
<img width="2129" height="678" alt="1AACB13D-CD82-4EDC-A0F5-4BF9E959D7C8_1_201_a" src="https://github.com/user-attachments/assets/9dfffb31-006a-4a1b-8101-6d9ed30b77ec" />

*open('datanilai.csv')* digunakan untuk membuka dan membaca file CSV kemudian *csv.reader* untuk membaca data yang ada di dalam file CSV, *for row in csv_reader* digunakan untuk membaca/menampilkan data CSV dengan rapi baris demi baris dan *nama.append(row)* digunakan untuk menyimpan data yang telah dibaca
<img width="1320" height="239" alt="455CBF67-1236-4E81-8D24-24CEB994EF5F_4_5005_c" src="https://github.com/user-attachments/assets/bcbf6773-c27b-4bf4-9f4f-095772355e6c" />

*for row in nama* digunakan untuk menampilkan data mahasiswa satu per satu dengan rapi, kemudian *elif* digunakan untuk memeriksa kondisi lain jika kondisi pada if sebelumnya tidak terpenuhi. Pada program ini, *elif* digunakan untuk menjalankan menu tambah data dan keluar sesuai pilihan user.
<img width="1436" height="563" alt="0A57DFAD-7655-4485-B863-C65FE2402AEC_1_201_a" src="https://github.com/user-attachments/assets/24023a3b-0657-4b09-a6a1-834643847037" />

*open('datanilai.csv', mode='a')* digunakan untuk membuka file dalam mode append agar data baru ditambahkan tanpa menghapus data lama. *csv.writer()* digunakan untuk menulis data baru ke dalam file CSV. *writer.writerow()* digunakan untuk menyimpan data nilai baru, lalu *break* digunakan untuk menghentikan program ketika pengguna memilih menu keluar. Kemudian yang terakhir yaitu *else* digunakan jika kondisi if dan elif sebelumnya tidak terpenuhi. Pada program ini, else menampilkan pesan "Pilihan tidak valid!" ketika user memasukkan pilihan menu yang tidak sesuai.
<img width="1882" height="603" alt="EF8A0020-A237-4E81-9996-03D9F17E7138_1_201_a" src="https://github.com/user-attachments/assets/5e66996f-6117-469f-a9d2-0994d1895339" />


*2. OUTPUT*

Menu 1. Lihat Data Nilai
<img width="2463" height="1599" alt="E784B7F3-ED62-4924-95C4-42D9123029A0_1_201_a" src="https://github.com/user-attachments/assets/346e2ee2-7a0b-48d9-b054-813272985611" />


Menu 2. Tambahkan Data Nilai
<img width="2437" height="1646" alt="22B2DC0E-B820-4710-AFF2-8D804763C82E_1_201_a" src="https://github.com/user-attachments/assets/d5b52b78-a6e9-49f6-a33f-1e4b99d6d883" />

Data baru tersimpan setelah program dijalankan
<img width="2660" height="1670" alt="0696F953-10D3-424D-B618-60A2517E3181_1_201_a" src="https://github.com/user-attachments/assets/c0e7fd92-8f61-4165-8875-018d5819ddbf" />

Menu 3. Keluar
<img width="1124" height="358" alt="7F79D5DA-9F03-4EFC-BD6F-3CA4D40B451D_4_5005_c" src="https://github.com/user-attachments/assets/276bbfde-eaed-4843-89bc-1b1c95dfb7be" />





