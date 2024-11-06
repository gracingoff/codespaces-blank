# Gracin Goff
# UWYO COSC 1010
# 11/05/2024
# HW 03
# Lab Section: 10
# Sources, people worked with, help given to: 
# your
# comments
# here

day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

days_of_week = {'0':'Sunday','1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday'}

def first_jan(year):
    y = year - 1 
    day_one = (36 + y + (y // 4) - (y // 100) + (y//400)) % 7 
    return day_one

def leap_year(year):
    if (year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
        day_in_month[1] = 29
    else:
        day_in_month[1] = 28

def valid(month , day , day_one):
    if day > day_in_month[month - 1] or day <= 0:
        print('Not valid date')
        return None
    total_days = sum(day_in_month[: month - 1]) + day 
    day_of_week = (total_days + day_one - 1) % 7 
    return day_of_week

date_input = input("Enter a date in the format MM/DD/YYYY to find what day of the week it lands on")

date = []

date = date_input.split("/")

month = int(date[0])

day = int(date[1])

year = int(date[2])

leap_year(year)
day_one = first_jan(year)
day_of_week = valid(month, day , day_one)
weekday = 1
if day_of_week is not None:
    for key,value in days_of_week.items():
        if day_of_week == days_of_week[key]:
            print(f'{date} {key}')



        


    


    



