#filename: q04_determine_leap_year.py
#author: Yuan Siang
#created: 3/2/13
#modified: -
#description: Determine leap year
#Practical 02 Q4

#main
#prompt for year
yr = int(input("Enter year: "))
#check if yr is divisible by 4
if (yr%4==0):
#print results
    print("Leap")
else:
    print("Non-Leap")
