# exercise aritmeth operation

"""
1 please calculate modulus and floor division this quiz
> 9 / 5

2.  Rian want to stationery shop to buy a ballpoint pen.
    The price of 1 ballpoint pen is Rp 1.750 IDR.
    When rian to buy 1 dozen ballpoint and he pays 5 thousand notes.
    How much change did Rian recived?
"""

# exercise number 1
print("===EXERCISE 1===")
x = 9 % 5
y = 9 // 5

print(9,"%",5,"=",x,"\n",9,"//",5,"=",y)

# exercise 2
print("===EXERCISE 2===")

ballpoint = 1750
dozen = 12
pay = 5 * 5000

# process 
rian = pay - (ballpoint * dozen)

print("balance the money Rian: ", rian)