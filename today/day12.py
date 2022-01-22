# # remember method string
# ## startswith & endswith
# from posixpath import split


# name = "Putu Julinta"
# start_name = name.startswith("Putu")
# end_name = name.endswith("julianta")
# print(start_name)
# print(end_name)
# ## remember join() & split
# name = ["Komang", "Kadek", "Putu"]
# print(f'{name} type : {type(name)}')
# join_name = ". ".join(name)
# split_name = join_name.split(".")
# print(join_name)
# print(split_name)
# ## remember index string
# name = "Putu Julianta"
# print(name[0])
# print(name[-1])
# print(name[0:-1])
# # formating string
# ## normal vs use format string
# print('\n'+"Formating String".upper().center(20,"=")+'\n')
# ## normal vs use formating string
# ## for string & boolean
# name = "Julianta"
# print('Hallo my name is ' + name) # normal use operator (+)
# print(f'Hallo my name is {name}') # use formating
# ## for number (int & float)
# number = 10000
# a = -5
# b = 5
# c = 0.25
# print(f'{number:,}')
# print(f'{number:010}')
# print(f'{a:-}')
# print(f'{b:+}')
# print(f'{c:.0%}')
# print(f'{c:.1f}')
# # formating string width & aligment
# print(f'Width & Aligment'.center(20,'='))
# ## data
# name = "Julianta"
# weight = 70
# age = 19
# height = 172
# ## use normal
# print(name + '\n'+ str(weight) + '\n'+ str(age) + '\n'+ str(height)) # hardcore
# ## use format str
# print('\n' + 5*"=" +"Space" + 5*"=" + '\n')
# print(f'name = {name}\nage = {age}\nweight = {weight}\nheight = {height}')
# ## use format str
# print('\n' + 5*"=" +"Space" + 5*"=" + '\n')
# print(f'name = {name}\nage = {age}\nweight = {weight}\nheight = {height}')
# ## use format str for write mail
# print('\n' + 5*"=" +"Space" + 5*"=")
# print(f'''
# name   = {name}
# age    = {age:>8}
# weight = {weight:>8}
# height = {height:>8}
# ''')

# test library datetime
import datetime
import calendar
print("Please entered your:\nYear, Month, and Day !!!")
year = int(input('Year \t: '))
month = int(input('Month \t: '))
day = int(input('Day \t: '))
date_birth = datetime.date(year,month,day)
print(f'Your date of birth : {date_birth}')

today = datetime.date.today()
age_day = today - date_birth
age_year = age_day.days // 365
age_month =age_day.days % 365 // 30
print(f'Today : {today}\n')
print(f'You {age_year} years old, and {age_month} month')
print(f'The day is : {calendar.day_name[date_birth.weekday()]}')