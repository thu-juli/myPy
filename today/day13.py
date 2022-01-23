# control flow (continue, pass, break)
## pass
number = 0
print(f'The number now is: {number}')
while number < 5:
    number += 1
    print(f'The number now is: {number}')
    if number == 3:
        pass  # not execution (use as dummy)
print('finish\n')
## continue
print('continue'.upper().center(10))
number = 0
while number < 5:
    number += 1
    print(f'The number now is: {number}') # confition1
    if number == 3:
        print('Stop, watshupp')
        continue # jumping to condition1 looping
    print('whatsupp') # contition2
print('end program\n')
## break
number = 0
while number < 5:
    number += 1
    print(f'The number now is {number}')
    if number == 3:
        print('Nice')
        break
    print('Whatsupp')
print('End.')
## simple program use break
count = int(input('Count to : '))
number = 0
while True:
    number +=1
    print(f'{number}')
    if number == count :
        print(f'this is {count}')
        break
print('endprogram')    
