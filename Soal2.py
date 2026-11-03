
# SOAL 2 - DOUBLE LINKED LIST
# Simulasi Playlist Musik

# Membuat class Node
class Node:
    def __init__(self, judul, penyanyi, durasi):
        self.judul = judul
        self.penyanyi = penyanyi
        self.durasi = durasi
        self.prev = None
        self.next = None


# Membuat class Double Linked List
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # 1. Menambahkan lagu di akhir
    def tambah_lagu(self, judul, penyanyi, durasi):
        new_node = Node(judul, penyanyi, durasi)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        print("\nLagu berhasil ditambahkan!")

    # 2. Menghapus lagu di awal
    def hapus_lagu_awal(self):
        if self.head is None:
            print("\nPlaylist masih kosong!")
            return

        print("\nLagu dihapus:", self.head.judul)

        deleted_node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.current = None
        else:
            self.head = self.head.next
            self.head.prev = None

            if self.current == deleted_node:
                self.current = self.head

    # 3. Navigasi Next
    def next_lagu(self):
        if self.current is None:
            print("\nPlaylist kosong!")
        elif self.current.next is not None:
            self.current = self.current.next
            print("\n>> NEXT")
            self.tampilkan_lagu_sekarang()
        else:
            print("\nSudah berada di lagu terakhir!")

    # 4. Navigasi Previous
    def previous_lagu(self):
        if self.current is None:
            print("\nPlaylist kosong!")
        elif self.current.prev is not None:
            self.current = self.current.prev
            print("\n<< PREVIOUS")
            self.tampilkan_lagu_sekarang()
        else:
            print("\nSudah berada di lagu pertama!")

    # Menampilkan lagu yang sedang diputar
    def tampilkan_lagu_sekarang(self):
        if self.current is None:
            print("Tidak ada lagu yang diputar.")
        else:
            print("Judul   :", self.current.judul)
            print("Penyanyi:", self.current.penyanyi)
            print("Durasi  :", self.current.durasi, "menit")

    # 5. Menampilkan seluruh daftar lagu
    def tampilkan_playlist(self):
        if self.head is None:
            print("\nPlaylist kosong!")
            return

        print("\n========== DAFTAR PLAYLIST ==========")

        temp = self.head
        nomor = 1

        while temp is not None:
            tanda = " <-- Sedang diputar" if temp == self.current else ""

            print(f"{nomor}. {temp.judul}")
            print("   Penyanyi:", temp.penyanyi)
            print("   Durasi  :", temp.durasi, "menit")
            print("   Prev    :", temp.prev.judul if temp.prev else "None")
            print("   Next    :", temp.next.judul if temp.next else "None")
            print(tanda)

            temp = temp.next
            nomor += 1

        print("=====================================")


# PROGRAM UTAMA

playlist = Playlist()

# Memasukkan minimal 5 lagu
playlist.tambah_lagu("Hati-Hati di Jalan", "Tulus", 4)
playlist.tambah_lagu("Komang", "Raim Laode", 4)
playlist.tambah_lagu("Sempurna", "Andra and The Backbone", 4)
playlist.tambah_lagu("Evaluasi", "Hindia", 3)
playlist.tambah_lagu("Akad", "Payung Teduh", 5)

# Menu program
while True:
    print("\n========== MENU PLAYLIST MUSIK ==========")
    print("1. Tambah Lagu di Akhir")
    print("2. Hapus Lagu di Awal")
    print("3. Next (Lagu Berikutnya)")
    print("4. Previous (Lagu Sebelumnya)")
    print("5. Tampilkan Seluruh Playlist")
    print("6. Tampilkan Lagu Sekarang")
    print("7. Keluar")
    print("=========================================")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        judul = input("Masukkan judul lagu: ")
        penyanyi = input("Masukkan nama penyanyi: ")

        try:
            durasi = float(input("Masukkan durasi lagu (menit): "))
            if durasi <= 0:
                print("Durasi harus lebih dari 0!")
                continue
        except ValueError:
            print("Durasi harus berupa angka!")
            continue

        playlist.tambah_lagu(judul, penyanyi, durasi)

    elif pilihan == "2":
        playlist.hapus_lagu_awal()

    elif pilihan == "3":
        playlist.next_lagu()

    elif pilihan == "4":
        playlist.previous_lagu()

    elif pilihan == "5":
        playlist.tampilkan_playlist()

    elif pilihan == "6":
        playlist.tampilkan_lagu_sekarang()

    elif pilihan == "7":
        print("\nTerima kasih telah menggunakan playlist!")
        break

    else:
        print("\nPilihan tidak valid!")
