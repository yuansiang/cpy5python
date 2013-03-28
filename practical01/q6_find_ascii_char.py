#filename: q6_find_ascii_char.py
#author: Yuan Siang
#created: 25/1/13
#modified: -
#description: Converts ASCII code to characters
#Practical 01.Q6

#main

#Prompt for the ASCII code
code = int(input("Enter the ASCII code (from 0 to 127): "))
#Check if it is an ASCII code
if (0<=code<=127):
#display the character
    print("The character of the ASCII code is " +chr(code))
else:
    print("INVALID! Restart application to continue")
#end
