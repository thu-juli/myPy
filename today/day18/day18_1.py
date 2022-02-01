# contoh penggunaan __init__ pada class

class Kalkulator:
    """Contoh kelas Kalkulator sederhana"""

    def __init__(self, i=12345):
        self.i = i

    def f(self):
        return 'Hello World!'

k = Kalkulator(i=1024)  # melakukan instantiation sekaligus mengisi atribut i jadi 1024
print(k.i)              # mencetak atribut i dari objek k dengan keluaran nilai 1024

# classmethod
class Kalkulator:
    """"contoh kelas Kalkulator sederhana"""

    def f(self):
        return 'Hello World'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return f'{angka1} + {angka2} = {angka1 + angka2}'

k = Kalkulator()
print(k.tambah_angka(1, 2))

#staticmethod
class Kalkulator:
    """"contoh kelas Kalkulator sederhana"""

    def f(self):
        return 'Hello World'

    @staticmethod
    def kali_angka(angka1, angka2):
        return f'{angka1} x {angka2} = {angka1 * angka2}'

a = Kalkulator.kali_angka(2, 3)
print(a)