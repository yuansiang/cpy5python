#filename: q11_find_gcd.py
#author: Yuan Siang
#created: 5/2/13
#modified: -
#description: Find the greatest common divisor of 2 integers
#Practical 02 Q11

#initialise n1 n2 and d
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
d = 0
#make d to be the smaller of the integers
if (n1>n2):
    d = n2
else:
    d = n1

#loop while either n1 or n2 shows a remainder
while (n1%d!=0 or n2%d!=0):
    d = d - 1

#print result
print d
