#filename: q5_compute_series.py
#author: Yuan Siang
#created: 22/2/13
#modified: -
#description: Compute a series
#Practical 03 Q5

#define function m_series(i)
def m_series(i):
    print ("i    m(i)") #print headers
    x=0.0 #define float x
    y = 1 #define int y
    while (y<=i):
        x=float(1/(2*y-1)) + x #break the function into parts
        x=x - float(1/(2*y+1))
        print("{0:<4} {1:.11f}".format(y, x*4)) #print out the result along with the respective (i)
        y = y+2 

#main
m_series(19)
