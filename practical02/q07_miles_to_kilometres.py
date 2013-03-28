#filename: q07_miles_to_kilometres.py
#author: Yuan Siang
#created: 4/2/13
#modified: -
#description: Convert miles to kilometres
#Practical 02 Q7

#main

#initialise miles and km (and miles2 and km2) and i
miles = 0
km = 0
miles2 = 0
km2 = 0
i = 1
#display header
print("Miles Kilometers Kilometers Miles")
#loop from 1 - 10
for i in range (1,11):
    miles = i
    km = i*1.609
    km2 = (i+3)*5
    miles2 = km2/1.609
    i=i+1
    #display results with format
    print("{0:<5.0f} {1:<10.3f} {2:<10.0f} {3:>-0.3f}".format(miles, km, km2, miles2))

#end
