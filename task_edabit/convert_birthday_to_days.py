"""
Create a function that takes the data fo birthday and returns the age in days.
Include leap year

"""
from datetime import date

def calc_age(day, month, year):
    today = date.today().strftime("%d %m %Y").split()
    dict_months={
        '1': 31 , 
		'2': 28,
		'3': 31,
		'4': 30,
		'5': 31,
		'6': 30,
		'7': 31,
		"8": 31,
		'9': 30,
		'10': 31,
		'11': 30,
		'12': 31	
    }
    leap_year=0
    for i in range(int(year), int(today[2])):
        for b in [a for a in range(0, int(today[2]), 4)]:
            if i==b:
                leap_year+=leap_year+1
    year_to_day = (int(today[2]) - int(year))*365-int(day)+leap_year
    month_to_day = 0
    for a in dict_months:
        if int(month) < int(a):
            year_to_day = year_to_day - dict_months[a]
    for i in dict_months:
        if int(today[1]) < int(i):
            month_to_day = month_to_day + dict_months[i]
    result = year_to_day+month_to_day+int(today[0])
    return result


input_day = input("Eneter day of your birthday: ")
input_month = input("Eneter number month of your birthday: ")
input_year = input("Eneter year of your birthday: ")
print(calc_age(input_day,input_month, input_year ))
