# exercise comparasion and logic operations

"""
1. --- 1+++5 --- 9+++19 ---
2. +++1 --- 5+++9 --- 19+++
"""

# input user
print("--- 1+++5 --- 9+++19 ---")
input_user = float(input("please input data follow in top rule: "))

# process 
answer = (1 < input_user < 5) or (9 < input_user < 19)

# result
print("your data entered:", answer)

print("==============")
# input user
print("+++1 --- 5+++9 --- 19+++")
input_user = float(input("please input data follow in top rule: "))

# process 
answer =(input_user < 1) or (5 < input_user < 9) or (input_user > 19)

# result
print("your data entered:", answer)

