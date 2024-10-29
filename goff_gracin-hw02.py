# Gracin Goff
# UWYO COSC 1010
# 10/29/2024
# HW 02
# Lab Section: 10
# Sources, people worked with, help given to: 
# your
# comments
# here


mors_dict = {'A': '.-','N': '-.','B': '-...',
'O': '---','C': '-.-.','P': '.--.',
'D': '-..','Q': '--.-','E': '.',
'R': '.-.','F': '..-.','S': '...',
'G': '--.','T': '-','H': '....',
'U': '..-','I': '..','V': '...-',
'J': '.---','W': '.--','K': '-.-',
'X': '-..-','L': '.-..','Y': '-.--',
'M': '--','Z': '--..'}


message = input("Give me a phrase and I will print it in morse code")


morse_code = " "
for character in message.upper():
    if character in mors_dict:
        morse_code += mors_dict[character]+ " "
    else:
        morse_code += " "



        
print(morse_code)
