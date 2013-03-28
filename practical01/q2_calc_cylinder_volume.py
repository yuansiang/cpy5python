#filename: q2_calc_cylinder_volume.py
#author: Yuan Siang
#created: 22/1/13
#modified: -
#description: Calculates the volume of a cylinder
#- Practical 01.Q2

#main

#import pi
from math import pi

#get length of cylinder
length = float(input("Enter length of cylinder: "))

#get radius of cylinder
radius = float(input("Enter radius of cylinder: "))

#calculate area
area = radius * radius * pi

#calculate and display volume
volume = area * length
print("The volume of this cylinder is " + "{0:0.1f}".format(volume))

#end
