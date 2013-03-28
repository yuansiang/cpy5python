#filename: q6_determine_prime.py
#author: Yuan Siang
#created: 22/2/13
#modified: -
#description: Generate prime number list
#Practical 03 Q6

#define function is_prime()
from math import sqrt
def isprime(n):
     for b in range(2,int(sqrt(n)+1)):
        if(n%b==0):
            return False
     return True

#main
i = 2 
h = 0 #h will be the amount of primes found
primelist = [] #initialise prime list
while (h != 1000): #loop till number of primes reach 1000
    if(isprime(i)==True):
        primelist.append(i) #if it is a prime, it is appended into array
        h = h + 1
    i = i + 1
tenths = 0
while (tenths!=1000): #print in tenths, then add 10 to the previous sum
    print(primelist[tenths], primelist[tenths+1], primelist[tenths+2], primelist[tenths+3], primelist[tenths+4], primelist[tenths+5], primelist[tenths+6], primelist[tenths+7], primelist[tenths+8], primelist[tenths+9])
    tenths = 10 + tenths
