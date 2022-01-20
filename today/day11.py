# print("remember type data".center(50,".").upper())
# print("str".center(20,"=").upper())
# a = "1"
# print(a)
# print(type(a))
# print("int".ljust(20,"=".capitalize()))
# a = 1
# print(a)
# print(type(a))
# print("float".rjust(20,"*").upper())
# a = 1.0
# print(a)
# print(type(a))
# print("Bool".rjust(20,"*").upper())
# a = True
# print(a)
# print(type(a))
# print("c_types".center(20,"*").title())
# from concurrent.futures import process
# from ctypes import c_double
# from traceback import print_tb
# a = c_double(1.1)
# print(a)
# print(type(a))
# print("input from user".upper())
# data = input("Please input your data: ")
# print(data, type(data))
# # casting data
# height = float(input("please input your height: "))
# print(height, type(height))
# # remember operation arithmetic 
# print("arithmetic".upper())
# print("formula for circle".title())
# radius_usr = float(input("please input radius for circle : "))
# phi = 3.14
# formula = phi * (2*radius_usr)
# print(f"this is result for area circle : {formula:,.2f}")
print("operation comparasion & logic".title().center(50,"="))
# +++3....7+++10....15+++
data = float(input("Please input number for range \n(# +++3....7+++10....15+++) : "))
process = data < 3 or 7 < data < 10 or data > 15
print(f"your data input is {process} : ")