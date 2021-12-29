# Arithmetic Operators

""""
Arithmetic in Python 
> (), **, *, /, %, //, +, -
"""
## PARENTHESIS
print("===PARENTHESIS===")
a = 10
b = 2
c = 5

result = a + b * c
print(a,'+',b,'*',c,"=", result) # This normal result because multiplication first operation
result = (a + b) * c
print("(",a,'+',b,")",'*',c,"=", result) # in parenthesis first operation

## EXPONENT
print("===EXPONENT===")
a = 2
b = 3
result = a ** b

print(a,'**',b,"=",result)

## MULTIPLICATION
print("===MULTIPLICATION===")
a = 2
b = 3
result = a * b

print(a,'*',b,"=",result)

## DIVISON
print("===DIVISON===")
a = 3
b = 2
result = a / b

print(a,'/',b,"=",result)

## MODULUS
print("===MODULUS===")
a = 10
b = 3
result = a % b

print(a,'%',b,"=",result)

## FLOR DIVISION
print("===FLOR DIVISION===")
a = 10
b = 3
result = a // b

print(a,'//',b,"=",result)

## INCREASE
print("===INCREASE===")
a = 10
b = 2
result = a + b

print(a,'+',b,"=",result)

# DECREASE
print("===DECREASE===")
a = 3
b = 2
result = a - b

print(a,'-',b,"=",result)
