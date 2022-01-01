# basic type data in python (integer, float, string, boolean)

# INTEGER
print("===INTERGER===")
data_int = 10
print("value on data_int:", data_int)  # Print value data_int
print("type data on data_int:", type(data_int)) # Print type data use on variable data_int

# FLOAT
print("===FLOAT===")
data_float = 10.0
print("value on data_float:", data_float)  # Print value data_float
print("type data on data_float:", type(data_float)) # Print type data use on variable data_float

# STRING
print("===STRING===")
data_str = "10"
print("value on data_str:", data_str)  # Print value data_str
print("type data on data_str:", type(data_str)) # Print type data use on variable data_str

# BOOLEAN
print("===BOOLEAN===")
data_bool = True  # Commend in type data boolean (True or False)
print("value on data_bool:", data_bool)  # Print value data_bool
print("type data on data_bool:", type(data_bool)) # Print type data use on variable data_bool

## Special Type data import in c_types
from ctypes import c_double
print("===CTYPES===")
data_double = c_double(10.0)
print("value on data_double:", data_double)  # Print value data_double
print("type data on data_double:", type(data_double)) # Print type data use on variable data_double
