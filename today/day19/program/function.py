def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print('='*20)
        print(f'Nama: {kontak["nama"]}')
        print(f'Email: {kontak["email"]}')
        print(f'Telepon: {kontak["telepon"]}')

def new_kontak():
    nama = input('Nama: ')
    email = input('Email: ')
    telepon = input('Telepon: ')
    kontak = {
        "nama" : nama,
        'email' : email,
        'telepon': telepon 
    }
    return kontak

def hapus_kontak(daftar_kontak):
    nama = input('Masukan nama kontak yang akan dihapus: ')

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if nama == kontak['nama']:
            index = i
            break
    
    if index == -1:
        print('Data yang anda cari tidak ditemukan')
    else:
        del daftar_kontak[index]
        print('Data berhasil dihapus')

def cari_kontak(daftar_kontak):
    search_nama = input('Masukan nama yang dicari: ')

    for kontak in daftar_kontak:
        nama = kontak['nama']
        if nama.lower().find(search_nama.lower()) != -1:
            print('='*20)
            print(f'Nama: {kontak["nama"]}')
            print(f'Email: {kontak["email"]}')
            print(f'Telepon: {kontak["telepon"]}')