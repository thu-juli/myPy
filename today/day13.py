# create a triangle with looping
# 1.use for loop
print('Start for')
base = 9

number = 0  # use as dummy
for i in range(base):
    number += 1
    print(number*'+')

print('end for')

# 2.use while
print('Start while')

number = 0  # use as dummy
while number < base:
    number += 1
    print(number*'+')

print('end while')


# 3.use while in (ood multiples)
print('Start odd')
number = 0  # use as dummy

while number < base:
    number += 1
    if number % 2:
        print(number*'+')
    else:
        continue

print('end odd')
# 4.create equilateral triangle
print('start equilateral triangle')
count = 1
space = int(base/2)

while True:
    if count%2 :
        print(space*' ','+'*count)
        count += 1
        space -= 1
    else:
        count +=1
    if count > base:
        break

print('end equilateral triangle')
# 5.create rombus
print('start rombus')
# base = 5
# count = 1
# space = int(base/2)

# while True:
#     if count%2 :
#         print(f'{space*" "}{"+"*count}')
#         count += 1
#         space -= 1
#     else:
#         count +=1
#     if count > base:
#         break

# count = base
# space = (count % 2) 
# while True:
#     if count % 2:
#         # print(f'{space*" "}{count*"+"}')
#         print(space*' ',(count*'+'))
#         space += 1
#         count -= 1
#     else:
#         count -= 1
#     if count == 0:
#         break

n = 6
for i in range(n):
    for x in range (n,i,-1):
        print(" ", end="")
    for x in range (2*i+1):
        print("+", end="")
    print()

for i in range (n-2,-1,-1):
    for x in range(n,i,-1):
        print(" ",end = "")
    for x in range (2*i+1):
        print("+",end ="")
    print()


print('end rombus')
