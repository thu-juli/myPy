# Program Management Kontak
import function

# List Kontak
daftar_kontak = []
daftar_kontak.append({
    "nama" : "Julianta",
    "email" : "thujuli037@gmail.com",
    "telepon" : "082987984658"
})

# Menu
while True:
    print("Menu".center(20,'='))
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Konta")
    print("0. Keluar")

    pilih_menu = input('pilih menu: '.title())
    if pilih_menu == '0':
        break
    elif pilih_menu == '1':
        function.display_kontak(daftar_kontak)
    elif pilih_menu == '2':
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)

print('Keluar dari program, sampai jumpa :)')
