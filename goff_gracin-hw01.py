# Gracin Goff
# UWYO COSC 1010
# 10-15-2024
# HW 01
# Lab Section: 10
# Sources, people worked with, help given to:
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student and their scores
# in different subjects.
#
# Student Data:

students = [
{"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
{"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
{"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
{"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]


#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.


# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

averages = {}
for student in students:
    total = student["scores"]["Math"] + student["scores"]["Science"] + student["scores"]["English"]
    average = total/3
    print(f"{student["name"]}'s average score is {average:.2f}")
    averages[student["name"]] = average
print(averages)

for key, value in averages.items():
    if value > 80: 
        print(f"{key}'s grade is above 80.")
    else:
        print(f"{key}'s grade is not above 80.")


