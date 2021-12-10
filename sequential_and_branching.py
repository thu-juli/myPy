"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata: "Budi, pergi ke toko membeli 1 susu dan jika ada telur beli 6 butir"')
print('Budi menjawab: "OK"')
print('Budi berangkat ke toko')
print('Dan budi mulai berbelanja')

# Percabangan
milks = 172
eggs = 5
print(f'Jumlah susu {milks} botol')
print (f'Jumlah Telur {eggs} butir')

if milks > 0:
    print('Beli 1 botol susu')
else:
    print('Budi tidak membeli susu')
if eggs > 5:
    print('Beli 5 butir telur')
else:
    print ("Budi tidak membeli telur")

print('Budi pulang ke rumah')
print('Budi memberikan hasil belanjanya ke ibu')
