
# SOAL 3 - QUEUE DAN SEARCHING
# Simulasi Sistem Antrian Pendaftaran Pasien Klinik

# Membuat class untuk data pasien
class Pasien:
    def __init__(self, id_pasien, nama, keluhan):
        self.id_pasien = id_pasien
        self.nama = nama
        self.keluhan = keluhan


# Membuat class Queue
class AntrianPasien:
    def __init__(self):
        self.antrian = []

    # 1. Menambahkan pasien ke antrian (Enqueue)
    def tambah_pasien(self, pasien):
        self.antrian.append(pasien)
        print("\nPasien berhasil ditambahkan ke antrian!")

    # 2. Melayani pasien (Dequeue)
    def layani_pasien(self):
        if len(self.antrian) == 0:
            print("\nAntrian pasien kosong!")
        else:
            pasien = self.antrian.pop(0)

            print("\nPasien sedang dilayani:")
            print("ID Pasien :", pasien.id_pasien)
            print("Nama      :", pasien.nama)
            print("Keluhan   :", pasien.keluhan)

    # Menampilkan seluruh antrian
    def tampilkan_antrian(self):
        if len(self.antrian) == 0:
            print("\nAntrian pasien kosong!")
        else:
            print("\n===== DAFTAR ANTRIAN PASIEN =====")

            for i, pasien in enumerate(self.antrian, start=1):
                print(f"\nNomor Antrian: {i}")
                print("ID Pasien :", pasien.id_pasien)
                print("Nama      :", pasien.nama)
                print("Keluhan   :", pasien.keluhan)

    # 3. Linear Search berdasarkan nama
    def linear_search(self, nama):
        for pasien in self.antrian:
            if pasien.nama.lower() == nama.lower():
                return pasien

        return None

    # 4. Binary Search berdasarkan nama
    def binary_search(self, nama):
        # Mengurutkan data berdasarkan nama
        data = sorted(self.antrian, key=lambda p: p.nama.lower())

        kiri = 0
        kanan = len(data) - 1

        while kiri <= kanan:
            tengah = (kiri + kanan) // 2

            if data[tengah].nama.lower() == nama.lower():
                return data[tengah]

            elif data[tengah].nama.lower() < nama.lower():
                kiri = tengah + 1

            else:
                kanan = tengah - 1

        return None


# PROGRAM UTAMA

klinik = AntrianPasien()

# Data pasien awal
klinik.tambah_pasien(Pasien("P001", "Andi", "Demam"))
klinik.tambah_pasien(Pasien("P002", "Budi", "Batuk"))
klinik.tambah_pasien(Pasien("P003", "Citra", "Sakit kepala"))
klinik.tambah_pasien(Pasien("P004", "Dina", "Flu"))
klinik.tambah_pasien(Pasien("P005", "Eko", "Nyeri perut"))


while True:
    print("\n===== SISTEM ANTRIAN PASIEN KLINIK =====")
    print("1. Tambah Pasien ke Antrian")
    print("2. Layani Pasien (Dequeue)")
    print("3. Cari Pasien (Linear Search)")
    print("4. Cari Pasien (Binary Search)")
    print("5. Tampilkan Seluruh Antrian")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        id_pasien = input("Masukkan ID Pasien: ")
        nama = input("Masukkan Nama Pasien: ")
        keluhan = input("Masukkan Keluhan: ")

        pasien_baru = Pasien(id_pasien, nama, keluhan)
        klinik.tambah_pasien(pasien_baru)

    elif pilihan == "2":
        klinik.layani_pasien()

    elif pilihan == "3":
        nama = input("Masukkan nama pasien yang dicari: ")

        hasil = klinik.linear_search(nama)

        if hasil:
            print("\nPasien ditemukan!")
            print("ID Pasien :", hasil.id_pasien)
            print("Nama      :", hasil.nama)
            print("Keluhan   :", hasil.keluhan)
        else:
            print("\nPasien tidak ditemukan!")

    elif pilihan == "4":
        nama = input("Masukkan nama pasien yang dicari: ")

        hasil = klinik.binary_search(nama)

        if hasil:
            print("\nPasien ditemukan!")
            print("ID Pasien :", hasil.id_pasien)
            print("Nama      :", hasil.nama)
            print("Keluhan   :", hasil.keluhan)
        else:
            print("\nPasien tidak ditemukan!")

    elif pilihan == "5":
        klinik.tampilkan_antrian()

    elif pilihan == "6":
        print("\nTerima kasih telah menggunakan sistem antrian klinik!")
        break

    else:
        print("\nPilihan tidak valid!")
