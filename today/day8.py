# remember comparasion and logic operations

"""
    1.---(-5)+++0---(5+++7)---10+++15
    2.+++(-5)---(0+++5)---7+++10----
"""

# exercise number 1
print("==EXERCISE 1==")
print("---(-5)+++0---(5+++7)---10+++15")
input_user = float(input("plese input follow the command above!!: "))

process_inputUser = (-5 < input_user < 0) or (5 <= input_user <= 7) or (10 < input_user < 15)

print("your input is: ", process_inputUser)

# exercise number 2
print("==EXERCISE 2==")
print("+++(-5)---(0+++5)---7+++10----")
input_user = float(input("plese input follow the command above!!: "))

process_inputUser = (input_user < -5) or (0 <= input_user <= 5) or (7 < input_user < 10)

print("your input is: ", process_inputUser)


