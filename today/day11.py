# arithmetic ((),**,*,/,//,%,-,+)
# comparasion (<,>,<=,>=,==,!=,is, is not)
# logic (not, or, and, xor(^))
# bitwise (~, |, &, ^) and shifting (<<, >>)

#  operarion bitwise
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
## method startswith & endswith
full_name = "Putu Julianta"
cek_start = full_name.startswith("Putu")
cek_end = full_name.endswith("julianta")
print(cek_start)
print(cek_end)
## method split() & join()
my_heart = ['i','love','you']
print(f'{my_heart} is {type(my_heart)}')
join_myHeart = " ehm ".join(my_heart)
split_myHeart =join_myHeart.split(" ehm ")
print(join_myHeart)
print(split_myHeart)
## method center(), ljust(), rjust() and strip()
hai = 'hai'
hai_center = hai.center(10)
hai_ljust = hai.ljust(10,"=")
hai_rjust = hai.rjust(10,"=")
strip_haiRjust = hai_rjust.strip("=")
print(hai_center)
print(hai_ljust)
print(hai_rjust)
print(strip_haiRjust)
# formating string spesific to number
print(f'\nformating string\n')
name = "Julianta"
print("hallo" + " " + name) # not use format
print(f'hallo {name}') # use format
# spesific to number
buy = 50000
print(f'{buy:,}')
# decimal 
decimal = 10.915
print(f'{decimal} or {decimal:.2f}')
# landing zero
print(f'{decimal:010}')
# show minus (-) and plus (+)
a = -5
b = 5
print(f'{a:-}')
print(f'{b:+}')
# show percent (%)
percent = 0.25
print(f'{percent:.2%}')