# OOP - Inheritance 
class Kalkulator:
    """contoh kalkulator sederhana, kelas ini tidak boleh dirubah"""

    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:
            print(f'kalkulator sederhana melebihi angka: {self.nilai}')
        return self.nilai

class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

metodeKelas = Kalkulator
print(metodeKelas.tambah_angka(metodeKelas, 6, 6))

statikKelas = Kalkulator.tambah_angka(Kalkulator, 5, 10)
print(statikKelas)

kk = KalkulatorKali()
a = kk.kali_angka(2, 3)
print(a)

b = kk.tambah_angka(5, 6)
print(b)

# Override
class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai
    
    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        return self.nilai

kk = KalkulatorKali()

b = kk.tambah_angka(5, 6)
print(b)

#Syntax super()
class KalkulatorTambah(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai