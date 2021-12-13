# Comparison Operation

# all results are boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# greater than >
print('===Greater Than====')
result = a > 3
print(a, ">", 3, '=', result)
result = b > 3
print(b, ">", 3, '=', result)
result = b > 2
print(b, ">", 2, '=', result)

# less than >
print('\n===Less Than====')
result = a < 3
print(a, "<", 3, '=', result)
result = b < 3
print(b, "<", 3, '=', result)
result = b < 2
print(b, "<", 2, '=', result)

# greater than or equal to >
print('\n===Greater Than or Equal To====')
result = a >= 3
print(a, ">=", 3, '=', result)
result = b >= 3
print(b, ">=", 3, '=', result)
result = b >= 2
print(b, ">=", 2, '=', result)

# less than or equal to >
print('\n===Less Than or Equal To====')
result = a <= 3
print(a, "<=", 3, '=', result)
result = b <= 3
print(b, "<=", 3, '=', result)
result = b <= 2
print(b, "<=", 2, '=', result)

# equal to
print('\n===Equal To====')
result = a == 4
print(a, "==", 4, "=", result)
result = b == 4
print(b, "==", 4, "=", result)

# not equal to
print('\n===Not Equal To====')
result = a != 4
print(a, "!=", 4, "=", result)
result = b != 4
print(b, "!=", 4, "=", result)

# object identity (is)
print('\n===Object Identity (Is)====')
x = 5
y = 5
result = x is y
print('value x =', x, ',id', hex(id(x)))
print('value y =', y, ',id', hex(id(y)))
print("x is y =", result)
x = 5
y = 6
result = x is y
print('value x =', x, ',id', hex(id(x)))
print('value y =', y, ',id', hex(id(y)))
print("x is y =", result)

# object identity (is not)
print('\n===Object Identity (Is Not)====')
x = 5
y = 5
result = x is not y
print('value x =', x, ',id', hex(id(x)))
print('value y =', y, ',id', hex(id(y)))
print("x is not y =", result)
x = 5
y = 6
result = x is not y
print('value x =', x, ',id', hex(id(x)))
print('value y =', y, ',id', hex(id(y)))
print("x is not y =", result)
