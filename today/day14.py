# learning from dicoding


a = 10
print(a, 'bertipe data: ', type(a))
b = 1.8
print(b, 'bertipe data: ', type(b))
c = 1+2j
print(c, 'bertipe data: ', type(c), 'apakah benar? ', isinstance(c,complex))
# deret finaboci
# x=[0]*10005;              #inisialisasi array 0 sebanyak 10005; x[0]=0
# x[1]=1;                   #x[1]=1
 
# for j in range(2,10001):
#       x[j]=x[j-1]+x[j-2]  # Fibonacci
# print(x[10000])
b = 100.1234567890123456789
print(b)
# tipe data list
x = [5,10,15,20,25,30,35,40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])
# list, tuple, set, and dictionary
## adding new value in list
a = [1,3,4]
print(a)
a[1] = 2 # value a[1] = 3 stack new value a[1] = 2
a.append(5)
print(a)
del a[0]
print(a)
## slicing
s = "Hello World!"
print(s[4]) 		#ambil karakter kelima dari string s
print(s[6:11]) 		#ambil karakter ketujuh hingga sebelas dari string s
# s[5]="d" 		#ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
s = "Halo Dunia!"	#ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print(s)
## tuple
b = (1,2,3,4)
print(b, 'type: ', type(b))
# b[0] = 2
print(b)
# set
c = {1,2,3,2,3,4,1} # duplicate not support
print(c, 'type data: ', type(c))
# print(c[0])
# dictionary
d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d['key'])
print(d)
d[1] = 'nilai'
print(d)
print('\n')
# Generates error
# print("d[2] = ", d[2]);
# casting

a = [1,2,3,3,2,1]
print(a)
print(set(a))
b = [[1,2],[3,4]]
print()
print(b)