# belajar Casting
# merubah dari suatu tipe data ke tipe data lainnya

dataInt = 0

dataFloat = float(dataInt)  # dibulatkan kebawah
dataInt2 = int(dataInt)
dataStr = str(dataInt)
dataBool = bool(dataInt)  # nilai False = 0, selain itu True

print('====INTEGER====')
print('dataFloat =', dataFloat, ',tipe =', type(dataFloat))
print('dataInt2 =', dataInt2, ',tipe =', type(dataInt2))
print('dataStr =', dataStr, ',tipe =', type(dataStr))
print('dataBool =', dataBool, ',tipe =', type(dataBool))

dataStr = 'ucup'

dataFloat = float(dataStr)  # dibulatkan kebawah
dataInt2 = int(dataStr)
dataStr = str(dataStr)
dataBool = bool(dataStr)  # nilai False = 0, selain itu True

print('====STRING====')
print('dataFloat =', dataFloat, ',tipe =', type(dataFloat))
print('dataInt2 =', dataInt2, ',tipe =', type(dataInt2))
print('dataStr =', dataStr, ',tipe =', type(dataStr))
print('dataBool =', dataBool, ',tipe =', type(dataBool))
