#filename: q01_check_even.py
#author: Yuan Siang
#created: 29/1/13
#modified: -
#description: Check if a number is odd or even
#Practical 02 Q1

#main
#prompt to get number
num = int(input("Enter number: "))

#check if number is odd or even
if num % 2 == 0:
#print results
    print("{0}".format(num) + " is even")
else:
    print ("{0}".format(num) + " is odd")

#end
