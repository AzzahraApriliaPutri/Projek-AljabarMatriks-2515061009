import azzahra009

A = [
    [1, 2, -7],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, -2, 7],
    [-4, 5, -6],
    [-7, -8, 1]
]

V = [2, 9, 10]

hasil_tambah = azzahra009.penjumlahan_matriks(A, B)
print("hasil penjumlahan matriks A + B:", )
for baris in hasil_tambah:
    print(baris)


hasil_kurang = azzahra009.pengurangan_matriks(A, B)
print("hasil pengurangan matriks A - matriks B:")
for baris in hasil_kurang:
    print(baris)


hasil_perkalian = azzahra009.perkalian_matriks_vektor(A, V)
print("hasil perkalian matriks A * Vector:", hasil_perkalian)


