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