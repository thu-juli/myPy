# remember string operations and manipulation 

fisrt_name = "ucup"
mid_name = "D"
end_name = "Fame"

full_name = fisrt_name +' ' + mid_name +"'" + end_name

print(full_name)

# checking str in str

name = "ucup"
status = name in full_name 

print (name + " in " + full_name + " is : " + str(status))

# multiple str

wkwk = 10 * "wk"
print(wkwk) # or

print(10 * "wk")

# length of str

print("how long this char " + full_name + " : " + str(len(full_name)))

# index str
full_name = fisrt_name +' ' + mid_name +"'" + end_name

print("index ke -0 : " + full_name[0])
print("index ke -0 ends : " + full_name[0:])
print("index ke -1 : " + full_name[-1])
print("index ke -1 : " + full_name[-1])
print("index range 0 to 3 : " + full_name[0:3]) # expented to print "ucup", reality print "ucup"
print("index range 0 to 3 : " + full_name[0:4]) # solution

# min & max

print("smallest characters in " + full_name + " :" + " " + min(full_name))
print("smallest characters in " + full_name + " :" + " " + max(full_name))

# check min & max work

# use cek in ASII Code

print("ASII Code for : " + str(ord(" ")))
print("ASII Code for : " + str(ord("u")))

# str method (introduction)

## .count() method returns the number of elements with the specified value

data = "otong surotong"
count = str(data.count("o"))

print("data : " + data + " " + str(data.count("o")))
print("data : " + data + " " + count)

## use method upper(), (convert str to Uppercase)  

meet = "hallo good morning"
print(meet)
print(meet.upper())

## use method lower(), (convert str to lowercase)  

meet = "Hi, How are you TOdayyy?"
print(meet)
print(meet.upper())
print(meet.lower())

# use isx 
meet = "hai"
# print(meet.islower())
# print(meet.isupper())

# still many string methods for is (exemple) 
# meet.isalpha > checking this str use all alphabet
# meet.isalnum > checking this str use alpahabet and number
# meet.isdecimal > checking this str use all number decimal
# meet.isspace > checking this str use space
# meet.istitle > checking this str a title

meet = "Hallo My "
print(meet.isalpha())
print(meet.isalnum())
print(meet.isdecimal())
print(meet.isspace())
print(meet.istitle())