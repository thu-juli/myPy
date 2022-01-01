# Casting input from user
print("===INPUT USER===")
input_user = input("please input random data: ") # this command to assigment variable from user

print("data:", input_user, "type", type(input_user))  # print value and type data from input_user
"""
All input from user always result in type data "string
Here, important use CASTING to convert type data
"""

# CASTING to INTEGER
# print("===INTEGER===")
# data_int = int(input_user)

# print("data:", data_int, "type", type(data_int)) # Error when input decimal, char or bool

# CASTING to FLOAT
# print("===FLOAT===")
# data_float = float(input_user)

# print("data:", data_float, "type", type(data_float)) # Error when char and bool

"""
Tips: convert to number use float because float can convert all number (deciman or non decimal)
"""

# CASTING to BOOLEAN
# print("===BOOLEAN===")
# data_bool = bool(input_user)

# print("data:", data_bool, "type", type(data_bool)) # this command use detect user input data on no input data

# CASTING to BOOLEAN ver2
print("===BOOLEAN===")
data_bool = bool(float(input_user))

print("data:", data_bool, "type", type(data_bool)) # this command math use user choose (yes/no) and error when user no input
