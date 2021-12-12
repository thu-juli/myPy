# chapter input data from user

# all type data from user "String"
print('====FROM USER====')
data = input("input data: ")
print('data value: ', data)
print('type data: ',type(data))

# casting to interger (must number no decimal)
print('====Generate Input String to Integer====')
dataInt = int(input('input number: '))
print('dataInt value: ', dataInt)
print('type dataInt: ', type(dataInt))

# trick get value interger from user input decimal
print('====When User Input Decimal====')
dataInt = int(float(input('input number: ')))
print('dataInt value: ', dataInt)
print('type dataInt: ', type(dataInt))

# generate to type data boolean
print('====Generate to Boolean====')
binary = bool(int(input('choose "0/1": ')))
print('binary value: ', binary)
print('type binary: ', type(binary))

# thanks
