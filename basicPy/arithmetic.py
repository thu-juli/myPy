# aritmetic operations

a = 10
b = 5

# addition +
results = a + b
print('====Addition====')
print(a, '+', b, '=', results)

# subtraction -
results = a - b
print('====Subtraction====')
print(a, '-', b, '=', results)

# multiplication *
results = a * b
print('====Multiplication====')
print(a, '*', b, '=', results)

# divison /
results = a / b
print('====Divison====')
print(a, '/', b, '=', results)  # type data auto generate to float

# exponentiation **
results = a ** b
print('====Exponentiation====')
print(a, '**', b, '=', results)

# modulus %
results = a % b
print('====Modulus====')
print(a, '%', b, '=', results)

# floor division //
results = a // b
print('====Floor Divison====')
print(a, '//', b, '=', results)  # floor function after division

# operation priority
print('====Operation Priority====')
# priority
"""
1. ()
2. **
3. * / % //
4. + -
"""
x = 3
y = 2
z = 4

results = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', results)

results = x + y * z
print(x, '+', y, '*', z, 'results =', results)

results = (x + y) * z
print('(', x, '+', y, ')', '*', z, 'results =', results)
