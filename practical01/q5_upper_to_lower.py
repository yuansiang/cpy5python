#filename: q5_upper_to_lower.py
#author: Yuan Siang
#created: 25/1/13
#modified: -
#description: Converts upper case letters to lower case letters
#Practical 01.Q5

#main

#Enter a single upper case letter
ltr = str(input("Enter a single UPPER-CASE letter: "))
#check if it is indeed one letter only
if(len(ltr)!=1):
    print("INVALID! Restart application to continue")
else:
#check if it is indeed uppercase
    if(65<=ord(ltr)<=90):
#convert uppercase to lowercase and print
        print("The letter in lowercase is: " +chr(ord(ltr)+32))
        
    else:
        print("INVALID! Restart application to continue")

#end

