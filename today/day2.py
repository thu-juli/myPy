# Exercises 

# 1. Convert Fahrenheit to Kelvin
## Use this formula 
""""
1 Convert Fahrenheit to Reamur
2 Convert Reamur to kelvin
"""
print("Start")
fahrenheit = float(input("Input temperature in Fahrenheit:"))  # Command for user to input data
print("Temperatue:", fahrenheit, "F") # Print "input data" from user

reamur = 4/9 * (fahrenheit-32) #  Variable process convert Fahrenheit to Reamur
kelvin = 5/4 * reamur + 273  # Variable process convert Reamur to Kelvin

print("Temperatue:", kelvin,"K") # Print result Fahrenheit to Reamur and Reamur to Kelvin
print("End.")


# 2. Convert Kelvin to Fahrenheit
## Use this formula
"""
1 Convert Kelvin to Celcius
2 Convert Celcius to Fahrenheit
"""

print("Start") # Start idea
kelvin = float(input("Input temperature in Kelvin:"))  # Command for user to input data

print("Temperatue:", kelvin, "K") # Print "input data" from user


celcius = kelvin - 273  # Convert kelvin to celcius
fahrenheit = 9/5 * celcius + 32  # Convert celcius to fahrenheit

print("Temperatue:", fahrenheit,"F") # Print result Fahrenheit to Reamur and Reamur to Kelvin
print("End.")

