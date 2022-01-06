# remember what did your learn yesterday

# bitwise or logic operation
# logic operation use for comparasion binary (0 and 1)
# or (|)
print("==(|)==")

a = 5
b = 6
c = 5 | 6

print("data a:", a, "binary", format(a, "08b"))
print("data b:", b, "binary", format(b, "08b"))
print("data c:", c, "binary", format(c, "08b"))

# AND
print("==(&)==")

a = 5
b = 6
c = 5 & 6

print("data a:", a, "binary", format(a, "08b"))
print("data b:", b, "binary", format(b, "08b"))
print("data c:", c, "binary", format(c, "08b"))

# NOT
print("==(~)==")

a = 5
b = 6
c = ~ 6

print("data a:", a, "binary", format(a, "08b"))
print("data b:", b, "binary", format(b, "08b"))
print("data c:", c, "binary", format(c, "08b"))

# XOR (use when your expect to result operation NOT )
print("==(^)==")

a = 0b00000101
b = 0b11111111
c = a ^ b

print("data a:  ", a, "binary", format(a, "08b"))
print("data b:", b, "binary", format(b, "08b"))
print("data c:", c, "binary", format(c, "08b"))
# assigment operation
# use for shorted assigment
a = 4  # for example

a = a + 5 # when you dont use assigment operation

print(a)
a = 4 

a += 5 # use assigment operation
print(a)

"""
    in assigment operation you can use all operation (arithmetic, comparasion, logic and binary, shifting(optional))
"""

# intoduction string
# all about string 

print("you can write string in double qoute")
print('you can write string in qoute')
print('when you write double qoute in type data string you can use combination double quote" and quote')
print("you can use special char \\ (backslash) \' \"")
# in python there many use of special characters
# special char common use

## backspace
print("this linee\b use backspace, (double 'e' write one 'e')")

## tab
print("this line use \t\ttab")

## newline
print("this line 1 \nline 2") # LF
print("this line 1 \rline 2") # CR 
print("this line 1 \r\nline 2") # CRLF

# use raw string when you create commend include special char
print("this no use raw string: \n \t \b (all special character executed)")
print(r"this use raw string: \n \t \b (all special character not executed)")

# you can write paragraf in one command 
print("""
line 1
line 2
line 3
line 4
""")