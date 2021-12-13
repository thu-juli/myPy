# Program Temperature Conversion

print('Convert Fahrenheit to Kelvin\n')
""" 
formula: firts, convert fahrenheit to celcius
then, convert celcius to kelvin or convert fahrenheit to reamur
and reamur to kelvin
"""

# choose advance, convert in reamur

fahrenheit = float(input('input temperature Fahrenheit:'))
print('temperature', fahrenheit, 'degress Fahrenheit')

# fahrenheit to reamur (4/9 (F-32))
reamur = ((4/9) * (fahrenheit-32))
# reamur to kelvin (5/4 R + 273)
kelvin = (((5/4) * reamur) + 273)

print('fahrenheit to kelvin is', kelvin, 'degress Kelvin')

# Kelvin to Fahrenheit
print('\nConvert Kelvin to Fahrenheit\n')
kelvin = float(input('input temperature Kelvin:'))
print('temperature', kelvin, 'degress Kelvin')

# Kelvin to Reamur 4/5 * (K-273)
reamur = ((4/5) * (kelvin-273))

# Reamur to Fahrenheit 9/4 * R + 32
fahrenheit = (((9/4) * reamur) + 32)
print('Kelvin to Fahrenheit is', fahrenheit, 'degress Fahrenheit')
