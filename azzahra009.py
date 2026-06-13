def penjumlahan_matriks(A, B):
    baris_A, kolom_B = len(A), len(A[0])
    baris_B, kolom_B = len(B), len(B[0])

    hasil = [[0 for _ in range(baris_A)] for _ in range(baris_A)]

    for i in range(baris_A):
        for j in range(kolom_B):
            hasil[i][j] = A[i][j] + B[i][j]
            
    return hasil


def pengurangan_matriks(A, B):
    baris_A, kolom_B = len(A), len(A[0])
    baris_B, kolom_B = len(B), len(B[0])

    hasil = [[0 for _ in range(baris_A)] for _ in range(baris_B)]

    for i in range(baris_A):
        for j in range(kolom_B):
            hasil[i][j] = A[i][j] - B[i][j]
            
    return hasil


def perkalian_matriks_vektor(A, V):
    baris_A = len(A)
    kolom_A = len(A)
    panjang_V = len(V)

    hasil = [0 for _ in range(baris_A)]  

    for i in range (baris_A):
        for j in range(kolom_A):
            hasil[i] += A[i][j] * V[j]

    return hasil


    



