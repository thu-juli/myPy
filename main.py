"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata: "Budi, pergi ke toko membeli 1 susu"')
print('Budi menjawab: "OK"')
print('Budi berangkat ke toko')
print('Dan budi mulai berbelanja')

# Percabangan
milk_of_count = 1
if milk_of_count > 0:
    print('Budi mengecek harga, dan uang mencukupi')
    print('Budi membeli 1 susu')
else:
    print('Budi melihat tidak ada susu')
    print('Budi tidak jadi membeli susu')

print('Budi pulang ke rumah')
print('Budi memberikan hasil belanjanya ke ibu')