"""
Perulangan membaca buku While Undefined Count
"""

jumlah_buku = 10
print('Ibu said:"Baca semua bukumu"')

buku_yang_dibaca = 0
print(f'Jumlah buku yang sudah saya baca {buku_yang_dibaca}')

buku_yang_dibaca_dipahami = 0
while buku_yang_dibaca < jumlah_buku :
    buku_yang_dibaca = buku_yang_dibaca + 1
    if buku_yang_dibaca_dipahami == 9:
        print(f'Buku ke {buku_yang_dibaca_dipahami + 1} belum paham')
    else:
        buku_yang_dibaca_dipahami = buku_yang_dibaca_dipahami + 1
        print(f'Buku ke {buku_yang_dibaca_dipahami } sudah paham')
print(f'Jumlah buku yang dibaca {buku_yang_dibaca}')
print(f'Jumlah buku yang dibaca dan dipahami {buku_yang_dibaca_dipahami}')