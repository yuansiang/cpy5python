#filename: q06_kilograms_to_pounds.py
#author: Yuan Siang
#created: 4/2/13
#modified: -
#description: Convert kilograms to pounds
#Practical 02 Q6

#main

#initialise kg and lbs and i
kg = 0
lbs = 0
i = 1
#display header
print("Kilograms Pounds")
#loop from 1 - 10
for i in range (1,11):
    kg = i
    lbs = i*2.2
    i=i+1
    #display results with format
    print("{0:<9.0f} {1:.1f}".format(kg, lbs))

#end
    
