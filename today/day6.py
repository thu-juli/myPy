# bitwise operation / binary operation

# OR (|)
a = 9
b = 5

c = 9 | 5

print("====OR====")
print("data:", a, "binary:", format(a,"08b"))
print("data:", b, "binary:", format(b,"08b"))
print("data:", c, "binary:", format(c,"08b"))

# AND (&)
c = 9 & 5

print("====AND====")
print("data:", a, "binary:", format(a,"08b"))
print("data:", b, "binary:", format(b,"08b"))
print("data:", c, "binary:", format(c,"08b"))

# NOT (~)
b = 99
c = ~b
print("====AND====")
print("data: ", b, "binary:", format(b,"08b"))
print("data:",c, "binary:", format(c,"08b"))

# when your intersted to NOT you can use this command
print("==NOT VALUE===")

d = 0b00000010
e = 0b11111111 # this variable use to convert variable "d" to another value use "XOR"

print("data:", d)
print("data:", d^e, "binary:", format(d^e, "08b"))

# shifting 
## shifting right(>>)
a = 8

print("== >> ==")
print("data:", a, "binary:", format(a,"08b"))
print("data:", a >> 2, "binary:", format(a >> 2,"08b"))

## shifting left(<<))
a = 8

print("== << ==")
print("data:", a, "binary:", format(a,"08b"))
print("data:", a << 2, "binary:", format(a << 2,"08b"))
