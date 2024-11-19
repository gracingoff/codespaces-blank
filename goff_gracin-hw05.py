# Gracin Goff
# UWYO COSC 1010
# 11/19/2024
# HW 05
# Lab Section: 10
# Sources, people worked with, help given to: 
# your
# comments
# here


import openpyxl 
from openpyxl.styles import Color , PatternFill
import string 
wb = openpyxl.workbook()
sheet = wb.active 
background = Color(rgb='ADD8E6')
fill = PatternFill(patterntype = 'solid', fgColor = background)
body = Color(rgb='00008B')
fill_b = PatternFill(patterntype = 'solid', fgColor = body)
eyes = Color(rgb='000000')
fill_e = PatternFill(patterntype = 'solid', fgColor = eyes)
white = Color(rgb='FFFFFF')
fill_w = PatternFill(patterntype = 'solid', fgColor = white)
mouth = Color(rgb = 'FF0000')
fill_r = PatternFill(patterntype = 'solid', fgColor = mouth)

cells_lb = ['A1','B2','C2','D2','E2','F2','G2','H2','I2','J2','K2','L2','M2','N2','O2','P2','Q2','R2','S2','T2','U2',]