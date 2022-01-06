# remember arithmetic operation

"""
    1. please create formula rectangle (area and around)
        > length
        > width
"""

# input 
print("==FORMULA RECTANGLE==")
length = float(input("please input length: "))
width = float(input("please input width: "))

# process 
area = length * width
perimeter = 2 *(length + width)

# result
print("==RESULT==")
print("area rectangle: ", area)
print("perimeter rectangle: ", perimeter)
