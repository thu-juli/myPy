# # learning from dicoding


# a = 10
# print(a, 'bertipe data: ', type(a))
# b = 1.8
# print(b, 'bertipe data: ', type(b))
# c = 1+2j
# print(c, 'bertipe data: ', type(c), 'apakah benar? ', isinstance(c,complex))
# # deret finaboci
# # x=[0]*10005;              #inisialisasi array 0 sebanyak 10005; x[0]=0
# # x[1]=1;                   #x[1]=1
 
# # for j in range(2,10001):
# #       x[j]=x[j-1]+x[j-2]  # Fibonacci
# # print(x[10000])
# b = 100.1234567890123456789
# print(b)
# # tipe data list
# x = [5,10,15,20,25,30,35,40]
# print(x[5])
# print(x[-1])
# print(x[3:5])
# print(x[:5])
# print(x[-3:])
# print(x[1:7:2])
# # list, tuple, set, and dictionary
# ## adding new value in list
# a = [1,3,4]
# print(a)
# a[1] = 2 # value a[1] = 3 stack new value a[1] = 2
# a.append(5)
# print(a)
# del a[0]
# print(a)
# ## slicing
# s = "Hello World!"
# print(s[4]) 		#ambil karakter kelima dari string s
# print(s[6:11]) 		#ambil karakter ketujuh hingga sebelas dari string s
# # s[5]="d" 		#ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
# s = "Halo Dunia!"	#ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
# print(s)
# ## tuple
# b = (1,2,3,4)
# print(b, 'type: ', type(b))
# # b[0] = 2
# print(b)
# # set
# c = {1,2,3,2,3,4,1} # duplicate not support
# print(c, 'type data: ', type(c))
# # print(c[0])
# # dictionary
# d = {1:'value','key':2}
# print(type(d))
# print("d[1] = ", d[1])
# print("d['key'] = ", d['key'])
# print(d)
# d[1] = 'nilai'
# print(d)
# print('\n')
# # Generates error
# # print("d[2] = ", d[2]);
# # casting

# a = [1,2,3,3,2,1]
# print(a)
# print(set(a))
# b = [[1,2],[3,4]]
# print()
# print(b)
# input from user
# number = int(input('Please input number: '))
# number = eval(input('Please input number: '))
# print(number, type(number))

# a = ['satu','dua', 'tiga']
# print(a)
# print(' '.join(a))
# # change string element
# string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
# print(string.replace("Coding", "Pemrograman", 1))
# use string checking
# while True:
#     name = input('Please input name: ')
#     if name.isalpha():
#         print(f'Hello {name}')
#         break
#     else:
#         print('Please enter correct name')
# # formating string
# # zfill() for number
# number = 5
# print(str(number).zfill(5))
# number = 300
# print(str(number).zfill(5))
# number = -0.69
# print(str(number).zfill(5))
# # zfill() for string
# string = 'im'
# print(str(string).zfill(5))
# string = 'your'
# print(str(string).zfill(5))
# string = 'my name is Julianta'
# print(str(string).zfill(5))
# operation for list, set and string
# len()

list1 = [1,3,3,5,5,7,7,9,9]
print(list1)
print(len(list1))
set1 = {1,3,3,5,5,7,7,9,9}
print(set1)
print(len(set1))
str1 = 'Hello World!'
print(str1)
print(len(str1))
# merge and replication
## merge
number = [2,4,6,8]
string = list('PYTHON')
merge = number + string
print(merge)
## replication
string = list('PYTHON')
print(string*2)
# range()
for i in range(5):
    print(i)
print('new code'.upper())
for x in range(1,11):
    print(x)
print('new code2'.upper())
for x in range(1,11,2):
    print(x)
# assign values to multiple data
## normal assigment for list and tuple
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
## simple assigmrnt for list and tuple
data = ['shirt', 'white', 'L']
apparel, color, size = data
data = ('shirt', 'white', 'L')
apparel, color, size = data
# data = ['shirt', 'white', 'L'] # From List
# apparel, color, size, price = data
# .short()
number = [100,10,5,9,1,3]
number.sort()
print(number)
string = ['a', 'b', 'z', 'y', 'x']
string.sort()
print(string)
# case sensitive
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()
print(kendaraan)
# how to fix case sensitive
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort(key=str.lower)
print(kendaraan)
