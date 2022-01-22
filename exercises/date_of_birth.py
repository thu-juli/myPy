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