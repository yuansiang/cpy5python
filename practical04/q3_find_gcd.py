#filename: q3_find_gcd.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Find greatest common divisor
#Practical 04 Q3

#define function gcd()
def gcd(m,n):
    if (m>=n):#make sure m is larger than n to make the following true
        if(m%n==0):
            return n
        else:
            gcd (n,m%n) #use recursion to find GCD
            return (m%n)
    else:
        print("Error! Please make m>+n!")
        quit()

#main
print(gcd(24,16))
print(gcd(255,25))
## 8
## 5