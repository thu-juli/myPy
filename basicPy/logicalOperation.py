# Logical Operation

# not, or, and, xor

# NOT
a = True
c = not a
print('====NOT====')
print('data a:', a)
print('>>NOT')
print('data c:', c)

# OR (When 1 variable True, result always True
print('====OR====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, "", 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, "", 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

# AND (result True, if all variable True)
print('====AND====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, "", 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, "", 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)

# XOR (result True, if 1 variable must True)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, "", 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, "", 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

