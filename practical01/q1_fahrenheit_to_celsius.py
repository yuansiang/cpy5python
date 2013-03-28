#filename: q1_fahrenheit_to_celsius.py
#author: Yuan Siang
#created: 22/1/13
#modified: -
#description: Converts fahrenheit to celsius - Practical 01.Q1

#main

#prompt to get temp in fahrenheit
fah= float(input("Enter temperature in fahrenheit: "))

#calculate celsius
cel = (5/9)*(fah-32)

#display
print ("The temperature in celsius is " + "{0:<10.1f}".format(cel))

#end



