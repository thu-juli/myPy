# learn from w3school.com
## Python list
fruits = ['apple','banana','cherry']
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[-1])
print(fruits[0:-1])
# replace
print(10*"=")
fruits = ['apple','banana','cherry']
fruits[0] = 'water melon'
print(fruits)
fruits = ['apple','banana','cherry']
fruits[0:2] = ['orange', 'melon']
print(fruits)
fruits = ['apple','banana','cherry']
fruits[0:1] = ['avocado', 'melon', 10]
print(fruits)
fruits = ['apple','banana','cherry']
fruits[0:2] = ['strawbery']
print(fruits)
# use method
fruits = ['apple','banana','cherry']
fruits.insert(1,'watermelon')
print(fruits)
## python addlist item (method list)
### .apped()
print(f'method list'.capitalize().center(20,'='))
fruits = ['apple','banana','cherry']
fruits.append('manggo')
print(fruits)
fruits = ['apple','banana','cherry']
fruits.insert(0,'avocado')
print(fruits)
fruits = ['apple','banana','cherry']
tropical =('mango', 'papaya')
fruits.extend(tropical)
print(fruits)
## python remove specified item