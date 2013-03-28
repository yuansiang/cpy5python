#filename: q4_sum_series.py
#author: Yuan Siang
#created: 22/2/13
#modified: -
#description: Compute a series
#Practical 03 Q4

#define function m_series(i)
def m_series(i):
    x=0 #define float x
    while (i>0):
        x = float(i/(i+1)) + x #make x be the function + what was previously x
        i=i-1 #decrease i till i =0
    return (x)

#main
print ("i         m(i)") #print headers
for i in range (1,21):
    #display results with format (4sf) in a table, loop till 20
    print("{0:<9} {1:.4f}".format(i, m_series(i)))
    i=i+1
