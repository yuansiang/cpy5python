#filename: q1_sum_series1.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Execute function sum_series1
#Practical 04 Q1

#define function sum_series(i)
def sum_series1(i):
    if i == 1:
        return 1 #do not proceed with recursion if i is 1 to prevent division by 0
    else:
       return 1/i + sum_series1(i-1) #make the function call itself and get smaller
#main
i = int(input("Enter a positive integer: "))
print(sum_series1(i))

## Enter a positive integer: 10
## 2.9289682539682538