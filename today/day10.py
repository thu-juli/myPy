# format str

# use format str for type data str
print("STR".center(20,"="))
name = "ucup"
data = "Hello " + name
print(data)  # use manipulation str

name = "ucup"
data = f"Hello {name}"
print(data)  # use format str (simply)

# use format str for type data boolean
print("Boolean".center(20,'='))
boolean = True
print(f"Bool = {type(boolean)}")
print(f'Boolean = {boolean}')
print(type(f'Boolean = {boolean}'))

# use format str for type data int or float 
print("number".upper().center(20,"="))
number = 15
print(f'number = {number}')
print(f'number = {number:d}')

bilion = 1000000
print(f'bilion = {bilion:,}')

## decimal
decimal = 10.5809
print(f'decimal = {decimal:.3f}')

# leading zero
decimal = 10.5809
print(f'decimal = {decimal:010.3f}')

# show plus (+) or minus (-)
minus = -10
plus = 1000000
print(f'minus = {minus:-}')
print(f'plus = {plus:+,.2f}')

# show percentase
percent = 0.45
print(f'percent = {percent}')
print(f'percent = {percent:.1%}')

# arithmetic operation in placeholder
print("aritmetic".capitalize().center(20,"="))
price = 10000
count = 5

print(f'i buy a fruit {price*count}')
print(f'i buy a fruit {price*count:,}')

# convert to another number system
number = 252
print(f'number decimal = {number}')
print(f'number binary = {bin(number)}')
print(f'number octa = {oct(number)}')
print(f'number hexadecimal = {hex(number)}')
