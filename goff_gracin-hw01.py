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

students = ({"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
{"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
{"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
{"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}})


#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.


# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.


# Dictionaries of scores for each student

alice = {"Math": 85, "Science": 90, "English": 78}

bob = {"Math": 70, "Science": 88, "English": 82}

charlie = {"Math": 92, "Science": 81, "English": 89}

david = {"Math": 60, "Science": 75, "English": 80}


# Average scores 

avg_alice = (alice['Math']+alice['Science']+alice['English'])/3

avg_bob = (bob['Math']+bob['Science']+bob['English'])/3

avg_charlie = (charlie['Math']+charlie['Science']+charlie['English'])/3

avg_david = (david['Math']+david['Science']+david['English'])/3


# New dictionary of average scores

avg_scores = {}

avg_scores['Alice'] = avg_alice

avg_scores['Bob'] = avg_bob

avg_scores['Charlie'] = avg_charlie

avg_scores['David'] = avg_david

print(avg_scores)


# Scores over 80 

for key, value in avg_scores.items():
    if value > 80:
        print(key)

