# # Yesterday

# #Tipe Data

# ## INTEGER
# a = 10  # Tipe data integer (Number) This is Variable

# print("===INTEGER===") # DECORATE
# print("Data a:", a)  # This Simple Command Print
# print("Type Data a:", type(a)) # Simple comand Print Type data

# ## FLOAT
# a = 10.0  # Tipe data Float (Decimal) This is Variable

# print("===FLOAT===") # DECORATE
# print("Data a:", a)  # This Simple Command Print
# print("Type Data a:", type(a)) # Simple comand Print Type data

# ## STRING
# a = "10"  # Tipe data string (text/char)This is Variable

# print("===STRING===") # DECORATE
# print("Data a:", a)  # This Simple Command Print
# print("Type Data a:", type(a)) # Simple comand Print Type data

# ## BOOLEAN
# a = True  # Tipe data bolean (True/False) This is Variable

# print("===BOOLEAN===") # DECORATE
# print("Data a:", a)  # This Simple Command Print
# print("Type Data a:", type(a)) # Simple comand Print Type data

# ## Special Tipe Data (From type data C)

# from ctypes import c_double
# a = c_double(10.0)

# print("===C_DOUBLE===") # DECORATE
# print("Data a:", a)  # This Simple Command Print
# print("Type Data a:", type(a)) # Simple comand Print Type data


# CASTING TYPE DATA

## CASTING INTEGER to FLOAT, STRING and BOOLEAN 

# data_int = 10
# print("===CASTING INTEGER===")
# print("Data:", data_int, ", type:", type(data_int)) # Print data_int

# data_float = float(data_int)  # casting to float
# data_str = str(data_int)  # casting to str
# data_bool = bool(data_int)  # casting to bool

# print("Data:", data_float, ", type:", type(data_float)) # Print data_float (Result Decimal)
# print("Data:", data_str, ", type:", type(data_str)) # Print data_str (Result number in type data string)
# print("Data:", data_bool, ", type:", type(data_bool)) # Print data_bool (Result False when value variabel is 0)

# ## CASTING FLOAT to INTEGER, STRING and BOOLEAN 

# data_float = 10.0
# print("===CASTING FLOAT===")
# print("Data:", data_float, ", type:", type(data_float)) # Print data_float

# data_int = int(data_float)  # casting to int
# data_str = str(data_float)  # casting to str
# data_bool = bool(data_float)  # casting to bool

# print("Data:", data_int, ", type:", type(data_int)) # Print data_int (Result Pure Number no decimal)
# print("Data:", data_str, ", type:", type(data_str)) # Print data_str (Result number in type data string)
# print("Data:", data_bool, ", type:", type(data_bool)) # Print data_bool (Result False when value variabel is 0)

# ## CASTING STRING to INTEGER, FLOAT and BOOLEAN 

# data_str = "" # Important when value string use ""
# print("===CASTING STRING===")
# print("Data:", data_str, ", type:", type(data_str)) # Print data_str

# # data_int = int(data_str)  # casting to int
# # data_float = float(data_str)  # casting to str
# data_bool = bool(data_str)  # casting to bool

# # print("Data:", data_int, ", type:", type(data_int)) # Print data_int (when value var data_str char/text result error)
# # print("Data:", data_float, ", type:", type(data_float)) # Print data_float (when value var data_str char/text result error)
# print("Data:", data_bool, ", type:", type(data_bool)) # Print data_bool (Result False when value in var none (""))

# ## CASTING BOOLEAN to INTEGER, FLOAT and STRING 

# data_bool = True #  value boolean is True or False
# print("===CASTING BOOLEAN===")
# print("Data:", data_bool, ", type:", type(data_bool)) # Print data_bool

# data_int = int(data_bool)  # casting to int
# data_float = float(data_bool)  # casting to float
# data_str = str(data_bool)  # casting to str

# print("Data:", data_int, ", type:", type(data_int)) # Print data_int (Result 1 = True, 0 = False)
# print("Data:", data_float, ", type:", type(data_float)) # Print data_float (Result 1 = True, 0 = False)
# print("Data:", data_str, ", type:", type(data_str)) # Print data_str (Result True = True in str, False = False in str)

# ==============================================
# Input From User

input_user = input("input your name:")  # Simple Command input and print test "input your name:"

print("data:", input_user, ", type", type(input_user)) # Result always type data STRING

# input_user_int = int(input_user)
# input_user_float = float(input_user)
input_user_bool_str = bool(input_user)
# input_user_bool_num = bool(float(input_user))

# print("data:", input_user_int, ", type", type(input_user_int)) # error when (user no input and input char)
# print("data:", input_user_float, ", type", type(input_user_float)) # error when (user no input and input char)
print("data:", input_user_bool_str, ", type", type(input_user_bool_str)) # result True when user "Input" and False when user "No Input" # Ver1
# print("data:", input_user_bool_num, ", type", type(input_user_bool_num)) # result False when user "Input 0" and Error when user "Input Char"# Ver2
