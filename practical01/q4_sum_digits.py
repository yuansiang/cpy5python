#filename: q4_sum_digits.py
#author: Yuan Siang
#created: 22/1/13
#modified: -
#description: Sums up the digits in an integer
#Practical 01.Q4

#main

#prompt for integer
num = int(input("Enter an integer between 0 to 1000: "))

#check the integer keyed in
if (num<10):
    print("Total sum of digits is: "+"{0}".format(num))
elif (0<num<1000):
#find value of integer in "ones"
    first=num%10
#get value of num without integer in "ones" place
    second = num // 10
#check if num is 3 digits or 2 digits
    if (second<10):
#print sum of digits in integer
        total = first + second
        print("Total sum of digits is: "+"{0}".format(total))
    else:
        third = second // 10
#find the value of second integer
        second = second - third*10
#calculate and show total sum
        total = first + second + third
        print("Total sum of digits is: "+"{0}".format(total))
else:
    print("Restart application to continue")

#end

    
