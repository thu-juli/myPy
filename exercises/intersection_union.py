# exercise comparasion and logic operations

"""
1. ---- (0 ++++ 5) ---- (8 ++++ 11) ----
2. ++++ 0 ---- 5 ++++ 8 ---- 11 ++++
"""
# exercise number 1
# input user 
print("===EXERCISE 1===")
input_user = float(input("please input value ((0 up to 5) or (8 up to 11) : "))

# process 
exercise1 = ( ((input_user > 0) and (input_user < 5)) or ((input_user > 8) and (input_user < 11)) )

# result
print("the data your entered:", exercise1)


# exercise 2
# ++++ 0 ---- 5 ++++ 8 ---- 11 ++++

# input
print("\n",10*"=","\n")
print("===EXERCISE 2===")
input_user = float(input("please input value ((less than 0) or (5 up to 8) or (more than 11)) : "))

# process
exercise2 = ( (input_user < 0) or ((input_user > 5) and (input_user < 8)) or (input_user > 11))

# result 
print("the data your entered:", exercise2)
