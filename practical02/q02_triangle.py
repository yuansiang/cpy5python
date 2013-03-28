#filename: q02_triangle.py
#author: Yuan Siang
#created: 29/1/13
#modified: -
#description: Check if a triangle is valid
#Practical 02 Q2

#main
#Prompt for the 3 sides
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
#check if side1 and 2 is bigger than side3
if (side1 + side2 > side3):
    #check if side2 and 3 is bigger than side1
    if(side2 + side3 > side1):
        #check if side1 and 3 is bigger than side2
        if(side1 + side3 > side2):
        #confirm valid triangle
            peri = side1+side2+side3
            print("Perimeter = " + "{0}".format(peri))
        else:
            print("Invalid triangle!")
    else:
        print("Invalid triangle!")
else:
    print("Invalid triangle!")
#end
