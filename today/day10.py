# method str

meet = "Hai, How Are You?"

print("this normal meet : " + meet)
print("this upper meet : " + meet.upper())
print("this lower meet : " + meet.lower())

print("how to check str use method is")
meet_title = meet.title()
meet_upper = meet.upper()
meet_lower = meet.lower()

# check
print(meet_title + " use " + "method title : " + str(meet_title.istitle()))
print(meet_upper + " use " + "method upper : " + str(meet_upper.isupper()))
print(meet_lower + " use " + "method lower : " + str(meet_lower.islower()))

# use startswith and endswith

full_name = "ucup sorotong"

print(full_name + " startswith " + "Ucu : " + str(full_name.startswith("Ucu")))
print(full_name + " endswith " + "otong : " + str(full_name.endswith("otong")))

# cek title

cek_title = "This Is Title".istitle()
print(cek_title)

## Use join() & split()
print("join() & split()")
love = ["i","love","you"]
print(love)

# use join()
full_love = " ".join(love)
print(full_love)

# use split()
full_love = "ihmlovehmyou"
print(full_love.split("hm"))

# allocated str use rjust(), ljust(), center()

print("text")
print("'"+"text".ljust(10)+"'")
print("text")
print("'"+"text".rjust(10)+"'")
print("text")
print("'"+"text".center(10,"=")+"'")

## back to normal 
text = "text".center(10)
print(text.strip())
