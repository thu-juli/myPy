# remember type data

# type data in python (integer, float, string, boolean)

# INTEGER 
print("===INTEGER===")
data_int = 10

print("data:", data_int,"type data:",type(data_int))

# FLOAT 
print("===FLOAT===")
data_float = 10.0

print("data:", data_float,"type data:",type(data_float))

# STRING 
print("===STRING===")
data_str = "10"

print("data:", data_str,"type data:",type(data_str))

# BOOLEAN
print("===BOOLEAN===")
data_bool = True

print("data:", data_bool,"type data:",type(data_bool))

# SPECIAL TYPE DATA
from ctypes import c_double

data_c_types = c_double(10.9)
print("data:", data_c_types,"type data:",type(data_c_types))


