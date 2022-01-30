# Fungsi - Argumen dan Parameter
def printinfo (*args, **kwargs):
    for a in args:
        print(f'argumen posisi {a}')
    for key, value in kwargs.items():
        print(f'argumen kata kunci {key}:{value}')

# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
# printinfo(j=8, k=9, 1, 2)
printinfo(*(2, 3), **{'i':7, 'j':8})

# fngsi anonim (lambda)
kali = lambda nilai1, nilai2: nilai1 * nilai2
print(f'Hasil: {kali(11, 21)}')
print(f'Hasil: {kali(2, 2)}')