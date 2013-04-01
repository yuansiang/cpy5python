#filename: q2_sum_series1.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Execute function sum_series2
#Practical 04 Q2

#define function sum_series2(i)
def sum_series2(i):
    if i == 1:
        return float(i/(2*i+1)) #use float to ensure that it does not output an integer
    else:
        return (i/(2*i+1)) + sum_series2(i-1) #using recursion, compute i/2i+1 +.....
#main
i = int(input("Enter a positive integer: "))
print(sum_series2(i))

## Enter a positive integer: 3
## 1.161904761904762