# arithmetic ((),**,*,/,//,%,-,+)
# comparasion (<,>,<=,>=,==,!=,is, is not)
# logic (not, or, and, xor(^))
# bitwise (~, |, &, ^) and shifting (<<, >>)

#  operarion bitwise
from itertools import count
from traceback import print_tb


a = 5
b = 1
c = a | b
d = a & b
e = ~ a
f = 1  # variable for xor 
g = a ^ f
print(f'{format(a,"08b")} = {a}')
print(f'{format(b,"08b")} = {b}')
print(f'{format(c,"08b")} = {c}')
print(f'{format(d,"08b")} = {d}')
print(f'{format(e,"08b")} = {e}')
print(f'{format(g,"08b")} = {g}')

print("\n" + "manipulations string".upper().center(30,"=") + "\n")
# how to concatenate multiple string (using operations +)
first_name = "Putu"
last_name = "Julianta"
full_name = first_name+ last_name
print(first_name +" "+ last_name)
# checking string in string  (use in)
## print("Julianta" in "Putu Julianta")
name = "Julianta"
check_name = name in full_name
print(check_name)
len_name = len(full_name)
print(len_name)
print(type(len_name))
# indexing 
full_name = "Putu Julianta"
print(full_name)
print(full_name[0])
print(full_name[-1])
print(full_name[0:])
print(full_name[0:7])
print(f'{min(full_name)} is {ord(" ")}')
print(f'{max(full_name)} is {ord("u")}')
full_name = "Putu Julianta"
count_fullName = full_name.count("u")
print(f'character "u" in {full_name} are {count_fullName}')
# remember method in python