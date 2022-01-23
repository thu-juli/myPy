# exerise make a simple calculator
'''
1. component req (number1, operator, number2, result)
2. user input (number1, operator, number2)
3. process = number1 operatoer number2
3.1 operator use elif
'''

print(17*'=')
print('simple calculator'.upper())
print(17*'=')
# input
number1 = float(input('Please input value for number1\t\t\t: '))
operator = input('Please input operator arithmetic (+,-,x,/) \t: ')
number2 = float(input('Please input value for number2\t\t\t: '))
# process and result
if operator == '+':
    result = number1 + number2
    print(f'Your result : {result:.2f}')
elif operator == '-':
    result = number1 - number2
    print(f'Your result : {result:.2f}')
elif operator == 'x' or operator == '*':
    result = number1 * number2
    print(f'Your result : {result:.2f}')
elif operator == '/':
    result = number1 / number2
    print(f'Your result : {result:.2f}')
else:
    print('Please enter the correct operator!!!')
