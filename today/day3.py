# aritmeth operation
# in python availible artitmeth operation ((),**,*,/,%,//,+,-)

"""
() > Parenthesis use piority number 1
** > Use Exponent 
* > Use Multiple
/ > Use Division
% > Use Modulus
// > Use Flor Division
+ > Use increase
- > Use decrease
"""

# Exercise day3
# Convert day to time
"""
Input
1. Command to user input day 

Process
1. Process day to hours, minute and sec

Result
1. Day in hours, minute and sec
"""
print("===Convert day to time===")
input_user = float(input("input day your choose(in number): ")) # Input and convert in same command

in_hour = input_user * 24
in_minute = in_hour * 60
in_sec = in_minute * 60

print("==RESULT==")
print("day in hours:", in_hour, "h")
print("day in minutes:", in_minute, "m")
print("day in seconds:", in_sec, "sec")
