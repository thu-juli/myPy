# exercise comparasion and logic operations

"""
1. ---- (0 ++++ 5) ---- (8 ++++ 11) ----
2. ++++ 0 ---- 5 ++++ 8 ---- 11 ++++
"""

# exercise no 1
input_user = float(input("===>masukan nilai (> 0 < 5 atau > 8 < 11) : "))  # Input from user

## Process

process1 = ((input_user > 0) and (input_user < 5)) or ((input_user > 8) and (input_user < 11))
print("Value 1:", process1)
