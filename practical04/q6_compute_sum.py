#filename: q6_compute_sum.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Compute sum of sigits in integer
#Practical 04 Q6

#define function sum_digits(n)
def sum_digits(n):
    if n<10:
        return n
    else:
        return n%10 + sum_digits(n//10)
#main
n = int(input("Enter a positive integer: "))
print(sum_digits(n))
## Enter a positive integer: 11111111111
## 11

