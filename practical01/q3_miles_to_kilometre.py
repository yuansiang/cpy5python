#filename: q3_miles_to_kilometre.py
#author: Yuan Siang
#created: 22/1/13
#modified: -
#description: Converts miles to kilometres
#Practical 01.Q3

#main

#prompt to get distance in miles
miles = float(input("Enter distance in miles: "))

#calculate distance in km
km = miles*1.60934

#display distance in km
print("The distance in km is " + "{0:0.3f}".format(km)+".")

#end
