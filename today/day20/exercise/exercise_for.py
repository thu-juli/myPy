# Program membaca semua buku

# INPUT
books_count = 10
books_read = 0

# PROCESS
print(''.center(30,'='))
print(f'Jumlah buku budi: {books_count}'.title().center(30))
print(''.center(30,'='))
print('Ibu berkata: "Budi baca semua bukumu"')

books = input('Apa budi sudah membaca semua buku (sudah/belum): ')
if books == 'belum':
    for books_read in range(0, books_count):
        books_read += 1
        print(f'Budi membaca buku ke {books_read}')
        if books_read == books_count:
            print(f'Budi sudah membaca {books_read} buku dari {books_count} buku yang ada')
elif books == "sudah":
    books_read = 10
    print(f'Budi sudah membaca sebanyak {books_read} buku dari {books_count} buku yang ada')
else:
    print('Budi hanya dapat (sudah/belum)')