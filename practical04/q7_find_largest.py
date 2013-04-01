#filename: q7_find_largest.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Find the largest digit in an array
#Practical 04 Q7

#define function find_largest(alist)
def find_largest(alist):
    if(len(alist)==1): #case for if the list has only 1 integer
        return alist[0]
    elif(len(alist)==2): #case for if list has 2 integers
        if(alist[0]>alist[1]):
            return alist[0]
        else:
            return alist[1]
    else:
        if (alist[0]>alist[1]): #make the smaller number identical to be bigger one, then do recursion
            alist[1]=alist[0]
        return find_largest(alist[1:])
#main
alist=[]
end = int(input("Enter number of integers to be keyed in: "))
i=0
while (i!=end): #while loop till the loop is fulfilled
    alist.append(int(input("Enter positive integer: "))) #append into array
    i = i+1

print (find_largest(alist))

## Enter number of integers to be keyed in: 4
## Enter positive integer: 2332
## Enter positive integer: 2425
## Enter positive integer: 25222
## Enter positive integer: 2323
## 25222