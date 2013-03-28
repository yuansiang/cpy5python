#filename: q2_display_pattern.py
#author: Yuan Siang
#created: 21/2/13
#modified: 22/2/13
#description: Display pattern of 'triangle' till n
#Practical 03 Q2
import sys
if (sys.version_info>=(3,0,1)):
  sys.stderr.write("You need python 2 to run this script\n")
  exit()
else:
    #initialise empty array bloc[]
    bloc= []
    #define function display_pattern
    def display_pattern(n):
        a=1 #initialise an int a which begins from 1
        while (a!=n+1):
            bloc.insert(0,a)
            a = a+1 #n remains fixed but a keeps increasing till it reaches n
            print ("{:>100}".format(bloc, 100)).replace('[', '').replace("]", '').replace(",", ' ')
                #print out the result, formatting to the right and replacing the []s and ,s of array   

    #main
    x = int(input("Enter an integer :")) #prompt for integer
    display_pattern(x)
