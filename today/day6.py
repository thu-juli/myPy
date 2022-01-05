# introduction string

# how to write command string in python
"""
    1. use quote ('')
    2. use double quote("")
"""

print('this string uses quote')
print("this string uses double quote")

# how to write "" or '' in python?
print("hai, 'my name is!'")
print('Budi speaks:"hai, ....."')

# use special char to input 1 quote/double quote

print("this command to print \' or it\'s")
# special char can use create 
## backslash (\)
print("how to print backslash (\\)")

# tab
print("how to print tab (\t\t\t)")

# backspace 
print("how to print backspace (back \bspace)")

# newline
print("how to print newline \n(this line 2)") # line feed (use in os UNIX, Linux, or MacOS)
print("how to print newline \r(this line 2)") # carrige return
print("how to print newline \r\n(this line 2)") # CRLF (carrige return line feed) use in WinOS

# use string literal or raw
# when you no use string raw
print("C:\new folder") # results are not expected
print(r"C:\new folder") # its work when use string raw

# multiline literal 

print("""
yo
whats up bro!
""")

# multiline literal with string raw

print(r"""
yo \n this newline or inline
hohhhhoo \n\t\b\r\r\n
""")
