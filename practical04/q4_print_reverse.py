#filename: q4_print_reverse.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Reverse the digits of an integer
#Practical 04 Q4

#define function reverse_int(n)
def reverse_int(n):
    if (n<10): #considering cases where n is single digit
        print (n)
    else:
        print(n%10, end='') #use modulus to obtain last number of integer
        reverse_int(n//10) #remove last number of integer and repeat

#main
n = int(input("Enter a positive integer:"))
reverse_int(n)
## Enter a positive integer:12425
## 52421