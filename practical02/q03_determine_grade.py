#filename: q03_determine_grade.py
#author: Yuan Siang
#created: 3/2/13
#modified: -
#description: Determine grade 
#Practical 02 Q3

#main
#prompt for grade
grade = int(input("Enter score: "))
#check if grade is from 0 to 100
if(grade<0 or grade>100):
    print("Invalid! Score must be within 0 - 100.")
else:
    #calculate respective grade
    if (70<=grade<=100):
        print ("A")
    elif (60<=grade<=69):
        print ("B")
    elif(55<=grade<=59):
        print("C")
    elif(50<=grade<=54):
        print("D")
    elif(45<=grade<=49):
        print("E")
    elif(35<=grade<=44):
        print("S")
    else:
        print("U")
#end
