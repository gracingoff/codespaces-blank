# Gracin Goff
# UWYO COSC 1010
# 11/05/2024
# HW 03
# Lab Section: 10
# Sources, people worked with, help given to: 
# your
# comments
# here

while True: 

    date_input = input("Give me a date in MM/DD/YYYY format and I will tell you what day of the week it lands on.")

    if date_input.upper() == "EXIT":
        break
    else:

        date = []

        date = date_input.split("/")

        month = date[0]
        day = date[1]
        year = date[2]

        month = int(month)
        day = int(day)
        year = int(year)


        y = year -1
#Jan first falls on day x where:
        jan_1 = (36 + y +(y/4) - (y/100) + (y/400))%7

        print(jan_1)

        months = {'Jan':'31','Feb':'28','Mar':'31','Apr':'30','May':'31','Jun':'30','Jul':'31','Aug':'31','Sep':'30','Oct':'31','Nov':'30','Dec':'31'}

        days_of_week = {'0':'Sunday','1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday'}

        if 0 >= jan_1 < 1:

         print(f'{date_input} is on {days_of_week['0']}')

        elif 1 >= jan_1 <2 :

            print(f'{date_input} is on {days_of_week['1']}')

        elif 2 >= jan_1 < 3:

            print(f'{date_input} is on {days_of_week['2']}')

        elif 3 >= jan_1 < 4:

            print(f'{date_input} is on {days_of_week['3']}')

        elif 4 >= jan_1 < 5:

            print(f'{date_input} is on {days_of_week['4']}')

        elif 5 >= jan_1 < 5:

            print(f'{date_input} is on {days_of_week['5']}')

        else:

            print(f'{date_input} is on {days_of_week['6']}')
        


    


    



