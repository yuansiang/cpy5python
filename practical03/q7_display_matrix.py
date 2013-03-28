#filename: q7_display_matrix.py
#author: Yuan Siang
#created: 22/2/13
#modified: -
#description: Display random matrix
#Practical 03 Q7

from random import * #import random

def print_matrix(n): #define function print_matrix()
    for i in range (0, n):
        for j in range (0, n):
            print (randint(0,1), end=" ") #print the random integer, with format
        print()

n = int(input("Enter a positive integer: ")) #prompt for integer n
print_matrix(n)
