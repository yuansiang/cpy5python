#filename: q2_sum_series1.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Execute function sum_series2
#Practical 04 Q2

#define function sum_series(i)
def sum_series2(i):
    if i == 1:
        return float(i/(2*i+1))
    else:
        return (i/(2*i+1)) + sum_series2(i-1)
#main
i = int(input("Enter a positive integer: "))
print(sum_series2(i))