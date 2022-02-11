daftar_buku = ['Matematika', 'IPS', 'IPA']

print('\nTampilkan mengunakan perintah Print')
print(daftar_buku)

print('\nPrint menggunakan indexing')
print(daftar_buku[0])

print('\nPrint menggunakan FOR index')
for buku in daftar_buku:
    print(buku)

print('\nPrint menggunkan FOR in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


daftar_buku = ['Matematika', 'IPS', 'IPA']
print('\nMenampilkan kembali variable daftar_buku')
print(daftar_buku)

print('\nMenambahkan daftar buku baru')
daftar_buku.append('4DX')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['Matematika', 'IPS', 'IPA', '4DX']
print('\nMenampilkan kembali variable daftar_buku')
print(daftar_buku)

print('\nMenghapus menggunakan pop sekaligus simpan di variable baru')
daftar_buku_baru = daftar_buku.pop(0) # pop hanya bisa diisi 1 parameter
for i in range(0, len(daftar_buku)): # hasilnya buku matematika hilang karena method pop
    print(daftar_buku[i])

print(daftar_buku_baru)

daftar_buku = ['Matematika', 'IPS', 'IPA', '4DX']
print('\nMenampilkan kembali variable daftar_buku')
print(daftar_buku)

print('\nMenghapus data mengunakan func del')
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\ndel [start:end:step]')
daftar_buku = ['Matematika', 'IPS', 'IPA', '4DX']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nMembuat varibale baru menggunakan varible lama')
daftar_buku = ['Matematika', 'IPS', 'IPA', '4DX']
daftar_buku_baru = daftar_buku[:]

del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List baru dengan list yang lama')
daftar_buku = ['Matematika', 'IPS', 'IPA', '4DX']
print(daftar_buku)
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])