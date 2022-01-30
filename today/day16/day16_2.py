def cetak(i):
    "Func change perintah print(_)"
    print(i)
    return

cetak('Fisrt Summon')
cetak('Second Summon')

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print(f'Dicetak dari dalam fungsi: {hasil}')
    return hasil

keluaran = kali(10, 20)
print(f'Dicetak sebagai kembalian: {keluaran}')

def kuadrat(x):
    # y = x*x
    return x*x

while True:
    value = int(input('Masukan angka yang mau dilihat pangkatnya: '))
    exponent = kuadrat(value)
    print(f'Nilai exponentnya: {exponent}')
    break

def ubah(list_saya):
    list_saya.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(list_saya))
 
# Panggil fungsi ubah
list_saya = [10, 20, 30]
ubah(list_saya)
print('Nilai di luar fungsi: {}'.format(list_saya))

print('\n')
def ubah(list_saya):
    list_saya = [1, 2, 3, 4]
    print(f'Ini nilai list_saya di dalam fungsi: {list_saya}')

list_saya = [10, 20, 30]
ubah(list_saya)
print(f'Ini nilai list_saya diluar fungsi: {list_saya}')
