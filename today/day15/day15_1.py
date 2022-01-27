# operator, operands and Expressions
from operator import *

green = 5
yellow = 10
print(f'green marbles = {green}')
print(f'yellow marbles = {yellow}')
for func in (lt, le, eq, ne, ge, gt):
    print(f'{func.__name__} (green, yellow): {func(green, yellow)}')
