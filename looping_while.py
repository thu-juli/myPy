"""
Perulangan membaca buku While
"""

jumlah_buku = 10
print('Ibu said:"Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah kamu baca {jumlah_buku_yang_sudah_dibaca}')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f'Buku ke {jumlah_buku_yang_sudah_dibaca}')
print(f'Jumlah buku yang sudah kamu baca {jumlah_buku_yang_sudah_dibaca}')
