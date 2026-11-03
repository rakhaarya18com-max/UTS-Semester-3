class BarangToko:

    # Constructor
    def __init__(self, kode_barang, nama_barang, stok, harga):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.stok = stok
        self.harga = harga

    # Menambahkan stok
    def tambah_stok(self, jml):
        self.stok += jml
        print("Stok berhasil ditambahkan!")

    # Mengurangi stok
    def kurangi_stok(self, jml):
        if jml <= self.stok:
            self.stok -= jml
            print("Stok berhasil dikurangi!")
        else:
            print("Stok tidak mencukupi!")

    # Menghitung total harga
    def total_harga(self, jumlah):
        return self.harga * jumlah

    # Menampilkan informasi barang
    def tampil_info(self):
        print("\n===== INFORMASI BARANG =====")
        print("Kode Barang :", self.kode_barang)
        print("Nama Barang :", self.nama_barang)
        print("Stok        :", self.stok)
        print("Harga       : Rp", self.harga)
        print("Total Nilai : Rp", self.total_harga(self.stok))


# Menyimpan objek barang
daftar_barang = []

# Input jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Input data barang secara manual
for i in range(jumlah_barang):
    print(f"\nData Barang ke-{i+1}")

    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan stok barang: "))
    harga = int(input("Masukkan harga barang: "))

    barang = BarangToko(kode, nama, stok, harga)
    daftar_barang.append(barang)


# Menu utama
while True:
    print("\n===== MENU INVENTORI TOKO =====")
    print("1. Tampilkan semua barang")
    print("2. Tambah stok")
    print("3. Kurangi stok")
    print("4. Total nilai barang di gudang")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        for barang in daftar_barang:
            barang.tampil_info()

    elif pilihan == "2":
        kode = input("Masukkan kode barang: ")
        ditemukan = False

        for barang in daftar_barang:
            if barang.kode_barang == kode:
                jml = int(input("Masukkan jumlah stok tambahan: "))
                barang.tambah_stok(jml)
                ditemukan = True
                break

        if not ditemukan:
            print("Barang tidak ditemukan!")

    elif pilihan == "3":
        kode = input("Masukkan kode barang: ")
        ditemukan = False

        for barang in daftar_barang:
            if barang.kode_barang == kode:
                jml = int(input("Masukkan jumlah stok yang dikurangi: "))
                barang.kurangi_stok(jml)
                ditemukan = True
                break

        if not ditemukan:
            print("Barang tidak ditemukan!")

    elif pilihan == "4":
        total = 0

        for barang in daftar_barang:
            total += barang.total_harga(barang.stok)

        print("\nTotal nilai seluruh barang di gudang: Rp", total)

    elif pilihan == "5":
        print("Program inventori toko selesai.")
        break

    else:
        print("Pilihan tidak valid!")