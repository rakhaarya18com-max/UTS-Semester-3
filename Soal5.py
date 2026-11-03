
# SOAL 5 - LIST, DICTIONARY, SET, DAN TUPLE
# Program Inventaris Laboratorium Komputer

# 1. Dictionary untuk menyimpan data barang
# Tuple untuk menyimpan nama, kategori, dan jumlah

inventaris = {
    "B001": ("Komputer", "Elektronik", 15),
    "B002": ("Monitor", "Elektronik", 10),
    "B003": ("Keyboard", "Aksesori", 20),
    "B004": ("Mouse", "Aksesori", 25),
    "B005": ("Proyektor", "Elektronik", 3)
}

# 2. List untuk menyimpan urutan kode barang
daftar_kode = list(inventaris.keys())


# Fungsi menampilkan seluruh barang
def tampilkan_barang():
    print("\n========== DATA INVENTARIS ==========")
    print("Kode\tNama Barang\tKategori\tJumlah")

    for kode in daftar_kode:
        nama, kategori, jumlah = inventaris[kode]
        print(f"{kode}\t{nama}\t\t{kategori}\t{jumlah}")

    print("=====================================")


# 3. Fungsi menambahkan barang baru
def tambah_barang():
    kode = input("Masukkan kode barang: ").upper()

    # Mengecek apakah kode sudah digunakan
    if kode in inventaris:
        print("\nGagal! Kode barang sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ")
    kategori = input("Masukkan kategori barang: ")

    try:
        jumlah = int(input("Masukkan jumlah barang: "))

        if jumlah < 0:
            print("Jumlah tidak boleh negatif!")
            return

    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    # Menyimpan data dalam bentuk tuple
    inventaris[kode] = (nama, kategori, jumlah)

    # Menambahkan kode ke dalam list
    daftar_kode.append(kode)

    print("\nBarang berhasil ditambahkan!")


# 4. Fungsi mencari barang berdasarkan kode
def cari_barang():
    kode = input("Masukkan kode barang yang dicari: ").upper()

    if kode in inventaris:
        nama, kategori, jumlah = inventaris[kode]

        print("\nBarang ditemukan!")
        print("Kode Barang :", kode)
        print("Nama Barang :", nama)
        print("Kategori    :", kategori)
        print("Jumlah      :", jumlah)
    else:
        print("\nBarang tidak ditemukan!")


# 5. Fungsi menghitung total seluruh barang
def hitung_total():
    total = 0

    for data in inventaris.values():
        total += data[2]

    print("\nTotal seluruh unit barang:", total)


# 6. Fungsi menampilkan kategori tanpa duplikasi
def tampilkan_kategori():
    kategori = set()

    for data in inventaris.values():
        kategori.add(data[1])

    print("\nKategori barang yang tersedia:")
    for item in kategori:
        print("-", item)


# PROGRAM UTAMA

while True:
    print("\n===== SISTEM INVENTARIS LABORATORIUM =====")
    print("1. Tampilkan Seluruh Barang")
    print("2. Tambahkan Barang Baru")
    print("3. Cari Barang Berdasarkan Kode")
    print("4. Hitung Total Seluruh Unit Barang")
    print("5. Tampilkan Kategori Barang")
    print("6. Keluar")
    print("==========================================")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tampilkan_barang()

    elif pilihan == "2":
        tambah_barang()

    elif pilihan == "3":
        cari_barang()

    elif pilihan == "4":
        hitung_total()

    elif pilihan == "5":
        tampilkan_kategori()

    elif pilihan == "6":
        print("\nTerima kasih telah menggunakan program!")
        break

    else:
        print("\nPilihan tidak valid!")
