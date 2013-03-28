#filename: q1_display_reverse.py
#author: Yuan Siang
#created: 21/2/13
#modified: -
#description: Display an integer in reverse order
#Practical 03 Q1

#define function reverse_int
def reverse_int(x):
    a = 0 #define variable a
    while(x!=0): 
        a = a*10 + x%10 #increase 'a' by 10 times and add the concurrent digit behind
        x = x // 10 #remove last digit of x
    return a
    

#main
front = int(input("Enter any integer: "))
print (reverse_int(front)) #print result
