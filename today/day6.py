# CASTING FROM INPUT USER

# INPUT FROM USER
input_user = input("please input data: ")

# what is type data from user
print("your data entered:", input_user, "type data:", type(input_user))  # all type data from user char (str)

# casting manual in variable
user_bool = bool(input_user)

print("data input user casting to boolean: ", user_bool) # True when user input data and False when user no entered data

print("\n", 10*"=", "\n")

# casting in one commend 
input_user = bool(float(input("plese input data on binary (0 or 1): ")))

print("data your entered from user version 2:", input_user, "type data: ", type(input_user))  # casting bool version 2, False when user input 0 and True user entered 1


