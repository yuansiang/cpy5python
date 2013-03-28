#filename: q05_find_month_days.py
#author: Yuan Siang
#created: 3/2/13
#modified: -
#description: Find number of days in month
#Practical 02 Q5

#prompt for month and year
yr = int(input("Enter year: "))
mth = int(input("Enter month: "))
#initiate mth_word (month in word form) and days (no. of days in month)
mth_word = ["January", "February", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]
days = 0
#check for february
if (mth == 2):
    if(yr%4==0):
        days = 29
    else:
        days = 28
#check for other months
elif (mth == 1 or 3 or 5 or 7 or 8 or 10 or 12):
    days = 31
elif (mth == 4 or 9 or 6 or 11):
    days = 30

#print results
print(mth_word[mth-1] + " " + "{0}".format(yr) + " has " + "{0}".format(days) + " days.")
#end

