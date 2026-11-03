
# SOAL 4 - BUBBLE SORT

# Data nilai awal
nilai = [75, 90, 65, 85, 70, 95, 80]

# Fungsi Bubble Sort manual
def bubble_sort(data):
    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if data[j] > data[j + 1]:
                # Menukar posisi nilai
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# 1. Menampilkan nilai sebelum diurutkan
print("NILAI SEBELUM DIURUTKAN")
print(nilai)


# 2. Mengurutkan nilai menggunakan Bubble Sort
bubble_sort(nilai)


# 3. Menampilkan hasil pengurutan
print("\nHASIL PENGURUTAN BUBBLE SORT")
print(nilai)

# Mencari nilai tertinggi dan terendah
tertinggi = nilai[-1]
terendah = nilai[0]

# Menghitung rata-rata
rata_rata = sum(nilai) / len(nilai)

print("\nNILAI TERTINGGI :", tertinggi)
print("NILAI TERENDAH  :", terendah)
print("RATA-RATA       :", rata_rata)


# 4. Menambahkan nilai baru yaitu 88
print("\nMENAMBAHKAN NILAI BARU")

nilai.append(88)

print("Data setelah ditambahkan 88:", nilai)

# Mengurutkan kembali menggunakan Bubble Sort
bubble_sort(nilai)

print("\nHASIL AKHIR SETELAH DIURUTKAN KEMBALI")
print(nilai)

# Menghitung rata-rata setelah penambahan nilai
rata_baru = sum(nilai) / len(nilai)

print("NILAI TERTINGGI :", nilai[-1])
print("NILAI TERENDAH  :", nilai[0])
print("RATA-RATA BARU  :", rata_baru)
