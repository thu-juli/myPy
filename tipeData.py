# penamaan variabel di Python
x = 10  # penamaan variabel di Pthton

print('nilai x = ', x)

"""
x adalah variabel
= adalah assigment
10 adalah value
"""

# assigment indirect
# tipe data integer (angka tanpa koma)
dataInt = x
print('nilai nilaiZ =', dataInt)
print('-bertipe data =', type(dataInt))

# ini merupakan tipe data float (angka dengan koma)
dataFloat = 1.5
print('nilai dataFloat =', dataFloat)
print('-bertipe data =', type(dataFloat))

# ini merupakan tipe data string (kumpulan karakter)
dataString = "ucup"
print('nilai dataFloat =', dataString)
print('-bertipe data =', type(dataString))

# ini merupakan tipe data boolean (true/false)
dataBool = True
print('nilai dataBool =', dataBool)
print('-bertipe data =', type(dataBool))

# tipe data khusus
# tipe data complex
dataComplex = complex(5, 1)
print('nilai dataComplex =', dataComplex)
print('-bertipe data =', type(dataComplex))
