# Program membaca semua buku sampai paham

# INPUT
books_count = 10
books_read = 0
understood_book = 0

# PROCESS
print(''.center(30,'='))
print(f'Jumlah buku budi: {books_count}'.title().center(30))
print(''.center(30,'='))
print('Ibu berkata: "Budi baca semua bukumu"')

while books_read < books_count:
    books_read += 1
    if understood_book == 9:
        print(f'Buku ke {understood_book + 1} belum paham')
    else:
        understood_book += 1
        print(f'Buku ke {understood_book} sudah paham')

print(''.center(30,'='))
print(f'Budi sudah paham {understood_book} dari {books_count} buku')
print(''.center(30,'='))