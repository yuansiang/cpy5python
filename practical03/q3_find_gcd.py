#filename: q3_find_gcd.py
#author: Yuan Siang
#created: 22/2/13
#modified: -
#description: Find greatest common divisor
#Practical 03 Q3

#define function gcd()
def gcd (x, y):
    d = 0
    #make d to be the smaller of the integers
    if (x>y):
        d = y
    else:
        d = x

    #loop while either x or y shows a remainder
    while (x%d!=0 or y%d!=0):
        d = d - 1
    print ("The GCD of "+str(x)+" and "+str(y)+ " is " +str(d))
    #display results

#main
gcd (24,16)
gcd (255,25)
