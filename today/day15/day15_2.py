# # control flow
# height = int(input('Please input your height: '))
# if height > 160:
#     print('You can enter')
# else :
#     print('sorry, you can\'t enter')
# number = 67
# if number % 2 == 0:
#     print('even number')
# else:
#     print('odd number')
"""use elif
study case menilai nilai tugas siswa
"""
nilai = int(input('Masukan nilai tugas Anda: '))
if nilai>80:
    print("""
    Selamat! Anda mendapatkan nilai A
    Pertahankan!
    """)
elif nilai>70:
    print("""
    Hore, Anda mendapatkan nilai B
    Tingkatkan!
    """)
elif nilai>60:
    print("""
    Berjuang lagi, Anda mendapatakan nilai C
    Ayo, Semangat!
    """)
else:
    print("""
    Hmm, Anda mendapat nilai D
    Ayo belajar, jangan malas
    """)