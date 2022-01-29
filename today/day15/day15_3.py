# looping
## for


string = "Dicoding"
for alpha in string:
    print(f'{alpha}')

# flowers = ['rose', 'jasmine', 'orchid']
# for flower in flowers:
#     print(f'flower: {flower}')

## using index
flowers = ['rose', 'jasmine', 'orchid']
print(range(len(flowers)))
for index in range(len(flowers)):
    print(f'Flowers : {flowers[index]}')

## while
print('while'.upper().center(20,"="))
count = 0
print(f'Value of variable count: {count}')
while count < 7:
    print(f'Now value count is {count}')
    count += 1

print(f'Value of variable count: {count}')

## infinite looping
# while True:
#     num = input('Please enter a data: ')
#     print(f'data your entered : {num}')

## Nested Looping
star = 6
while True:
    if star>0:
        print(star*'*')
        star -= 1
    else:
        break

for i in range(0,6):
    for j in range(0,6-i):
        print('*',end='')
        
    print()

for i in range(0,6):
    for j in range(0,1+i):
        print('*',end='')
    print()
    
# control looping
## break
for i in range(0,6):
    for j in range(0,6):
        if j>i:
            print()
            break
        else:
            print("*",end='')
print()

### continue 
jumlahbaris = 10
baris = 0
bintang = 0
while baris < jumlahbaris:
    if (bintang) >= (baris+1):
        print()
        baris = baris+1
        bintang=0
        continue      ##saat masuk ke if, maka bagian print * diluar if tidak akan dijalankan, langsung ulang ke while
    print("*",end="")
    bintang= bintang+1
    
### else after for    
for n in range (2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        print(f'{n} is a primes')

print('New')
### else after while
n = 10
while True:
    n -= 1
    if n == 7:
        break
    print(n)
else:
    print(f'finish looping in {n}')

### Pass
def aFubc():
    pass

var1=""
while(var1!="exit"):
    var1=input("Please enter an integer (type exit to exit): ")
    print(int(var1))

from calendar import c
import sys
data=''
while(data!='exit'):
    try:
        data=input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))

## simple looping
number = [1, 2, 3, 4]
exponen = []
for n in number:
    exponen.append(n**2)
print(exponen)

## inline loop (comprehension)
number = [1, 2, 3, 4]
exponen = [n**2 for n in number]
print(exponen)

list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplicate = []
for a in list1:
    for b in list2:
        if a == b:
            duplicate.append(a)
print(duplicate)

list1 = ['d', 'i', 'c', 'o']
list2 = ['d', 'i', 'n', 'g']
duplikat = [a for a in list1 for b in list2 if a == b]
print(duplikat) # Output: ['d','i']

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)