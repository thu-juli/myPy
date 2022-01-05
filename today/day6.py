# assigment operations

# intro
print("==INTRO==")
a = 5
print("data a:", a)

a = a + 2  # this commend can be shortened
print("data a:", a)

a = 5 
a += 2
print("data a:", a) # this is short command (assigment operations)


# arithmetic operation
print("==ARITHMETIC==")
print("data a:", a)
a += 2
print("data a += 2:", a) # this result is 9 because in line #12 variable a += 2
a -= 2
print("data a -= 2:", a) # this result is 9 because in line #12 variable a += 2
a *= 2
print("data a *= 2:", a) # this result is 9 because in line #12 variable a += 2
a /= 2
print("data a /= 2:", a) # this result is 9 because in line #12 variable a += 2

## modulus & floor division
print(">> MODULUS & FLOOR DIVISION")
print("data a :", a)

a = 7
a %= 3
print("data a %= 3:", a)

a = 7
a //= 3
print("data a //= 3:", a)

## exponent 
print(">> EXPONENT")
a = 5
print("data a :", a)

a **= 3
print("data a **= 3:", a)

# boolean or logic operation
print("LOGIC OPERATION")
# OR
a = True
print("data a:", a)
a |= False
print("data a |= False:", a)

a = False
print("data a:", a)
a |= False
print("data a |= False:", a)

# AND
a = True
print("data a:", a)
a &= False
print("data a &= False:", a)

a = True
print("data a:", a)
a &= True
print("data a &= True:", a)

# XOR
a = True
print("data a:", a)
a ^= False
print("data a ^= False:", a)

a = True
print("data a:", a)
a ^= True
print("data a ^= True:", a)

# BITWISE OPERATION
print("==BITWISE OPERATION==")

a = 5
print("data a:", a, "binary:", format(a,"08b"))
a |= 3
print("data a |=3 :", a, "binary:", format(a,"08b"))

a = 5
print("data a:", a, "binary:", format(a,"08b"))
a &= 3
print("data a &=3 :", a, "binary:", format(a,"08b"))

a = 5
print("data a:", a, "binary:", format(a,"08b"))
a ^= 3
print("data a ^=3 :", a, "binary:", format(a,"08b"))

# SHIFTING 
print("==SHIFTING==")
a = 8
print("data a:", a, "binary:", format(a,"08b"))
a >>= 2
print("data a >>=3 :", a, "binary:", format(a,"08b"))

a = 8
print("data a:", a, "binary:", format(a,"08b"))
a <<= 2
print("data a <<=3 :", a, "binary:", format(a,"08b"))
