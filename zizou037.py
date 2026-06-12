def tambah_matriks(A, B):
    """Menambahkan dua matriks dengan ukuran yang sama."""
    baris = len(A)
    kolom = len(A[0])
    
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]

    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = A[i][j] + B[i][j]
    return hasil

def pengkurangan_matriks(A, B):
    """Mengurangkan matriks dengan ukuran yang sama."""
    baris = len(A)
    kolom = len(A[0])
    
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]

    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = A[i][j] - B[i][j]
    return hasil

def perkalian_matriks(A, B):
    """Menghitung perkalian antar matriks (dot product)."""
    baris_A = len(A)
    kolom_A = len(A[0])
    kolom_B = len(B[0])

    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]

    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

def transpose_matriks_A(A):
    """Menghasilkan transpose dari sebuah matriks."""
    baris = len(A)
    kolom = len(A[0])
    
    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]

    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = A[i][j]
    return hasil

def transpose_matriks_B(B):
    """Menghasilkan transpose dari sebuah matriks."""
    baris = len(B)
    kolom = len(B[0])
    
    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]

    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = B[i][j]
    return hasil

def perkalian_skalar(A,skalar):
    """Menghasilkan perhitungan perkalian skalar matriks"""
    baris = len(A)
    kolom = len(A[0])

    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]

    for i in range(baris):
        for j in range(kolom):
            hasil [i][j] = A[i][j] * skalar

    return hasil

