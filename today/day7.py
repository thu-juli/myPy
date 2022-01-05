# remember casting data from user

input_user = input("what's your fav number? ")
print("your number fav is", input_user, ",type data is", type(input_user))  # all input from user is string

# convert to another type data
number_fav = float(input_user)
print("your number fav is", number_fav, ",type data is", type(number_fav))

# convert in command 
study = bool(float(input("are you just learning python? (0/1)")))
print(study)