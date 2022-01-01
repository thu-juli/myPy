# CASTING TYPE DATA
# Casting type data can use convert type data to another type data

# INTEGER
print("===CASTING INTEGER===")
data_int = 10  # Assigment variable
print("data :", data_int, "type:", type(data_int))  # Print value data_int and print type data use on data_int

## CASTING
data_float = float(data_int)  # Convert int to float
data_str = str(data_int)  #  Convert int to str
data_bool = bool(data_int)  #  Convert int to boolean

## Time to print
print("data :", data_float, "type:", type(data_float))  # in decimal
print("data :", data_str, "type:", type(data_str))   # in char
print("data :", data_bool, "type:", type(data_bool))  # result False if value 0 and True else value 0

# FLOAT
print("===CASTING FLOAT===")
data_float = 10.0  # Assigment variable
print("data :", data_float, "type:", type(data_float))

## CASTING
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

## Time to print
print("data :", data_int, "type:", type(data_int))  # in number (non decimal)
print("data :", data_str, "type:", type(data_str))   # in char
print("data :", data_bool, "type:", type(data_bool))  # result False if value 0 and True else value 0

# STRING
print("===CASTING STRING===")
data_str = ""  # Assigment variable
print("data :", data_str, "type:", type(data_str))

## CASTING
# data_int = int(data_str)
# data_float = float(data_str)
data_bool = bool(data_str)

## Time to print
# print("data :", data_int, "type:", type(data_int))  # error when value decimal and char
# print("data :", data_float, "type:", type(data_float))   # error when char
print("data :", data_bool, "type:", type(data_bool))  # result False if value none("")

# BOLEEAN
print("===CASTING BOLEEAN===")
data_bool = False  # Assigment variable
print("data :", data_bool, "type:", type(data_bool))

## CASTING
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)

## Time to print
print("data :", data_int, "type:", type(data_int))  # result 0 when False and result 1 when True
print("data :", data_float, "type:", type(data_float))   # result 0 when False and result 1 when True
print("data :", data_str, "type:", type(data_str))  # result False when False and result True when True
