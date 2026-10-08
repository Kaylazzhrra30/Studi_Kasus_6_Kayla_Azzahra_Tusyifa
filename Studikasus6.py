import csv

while True:
    print("\n=== NILAI UJIAN MAHASISWA KELAS A 2026 ===")
    print("1. Lihat Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = []

        with open('datanilai.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                nama.append(row)

        print("\n=== NILAI UJIAN MAHASISWA KELAS A 2026 ===")

        for row in nama:
            print("Nama         :", row[0])
            print("NIM          :", row[1])
            print("Mata Kuliah  :", row[2])
            print("Nilai        :", row[3])
            print("\n")

    elif pilihan == "2":
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        matkul = input("Masukkan Mata Kuliah: ")
        nilai = input("Masukkan Nilai: ")

        with open('datanilai.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([nama, nim, matkul, nilai])

        print("\nData berhasil ditambahkan!")

    elif pilihan == "3":
        print("\n Selesai!")
        break

    else:
        print("\nPilihan tidak valid!")