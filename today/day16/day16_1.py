# Exception Handling

# error
# x = 1
# x / 0

# simple exception handling

zero = 0
try:
    x = 1 / zero
    print(x)
except ZeroDivisionError:
    print(f"tidak bisa membagi angka dengan nilai nol".title() )

try:
    with open('contoh_tidak_ada.py') as file:                   
        print(file.read())                          
except (FileNotFoundError, ):
    print('file tidak ditemukan')

d = {'ratarata': '10.0'}
try:
    print(f'rata-rata: {d["rata_rata"]}')
except KeyError:
    print('Key tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('Value or type tidak sesuai')

d = {'ratarata': '10.0'}
try:
    print(f'rata-rata: {d["ratarata"]/3}')
except KeyError:
    print('Key tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('Value or type tidak sesuai')

try:
    print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:         
    print('penangan kesalahan: {}'.format(e))

d = {'ratarata': '10.0'}
if 'total' not in d:                                                                                                                         
    raise KeyError('harus memiliki total') 