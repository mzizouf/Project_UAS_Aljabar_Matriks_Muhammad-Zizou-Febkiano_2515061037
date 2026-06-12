import zizou037

matriks_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriks_B = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

skalar = 3 

print("=== Hasil Perkalian Matriks ===")
hasil_kali = zizou037.perkalian_matriks(matriks_A, matriks_B)

for baris in hasil_kali:
    print(baris)

print("\n=== Hasil Penjumlahan Matriks ===")
hasil_tambah = zizou037.tambah_matriks(matriks_A, matriks_B)\

for baris in hasil_tambah:
    print(baris)

print("\n=== Hasil Tranpose Matriks ===")
hasil_tranpose_A = zizou037.transpose_matriks_A(matriks_A)
hasil_tranpose_B = zizou037.transpose_matriks_B(matriks_B)

for baris in hasil_tranpose_A:
    print(baris)

print("\n")
for baris in hasil_tranpose_B:
    print(baris)

print("\n=== Hasil Pengkurangan Matriks ===")
hasil_pengkurangan = zizou037.pengkurangan_matriks(matriks_A, matriks_B)

for baris in hasil_pengkurangan:
    print(baris)

print("\n=== Hasil Skalar Matriks ===")
hasil_skalarmatriks = zizou037.perkalian_skalar(matriks_A,skalar)

for baris in hasil_skalarmatriks:
    print(baris)