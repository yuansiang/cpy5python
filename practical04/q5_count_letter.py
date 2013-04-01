#filename: q5_count_letter.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Count the instances of a letter in a string
#Practical 04 Q5
from string import * #this to use the .find() function
def count_letter(string,ch):#define function count_letter
    if len(string)==1: #present a case for if there is only one letter
        if string == ch:
            return 1 #return 1 if string matches the character, else return 0
        else:
            return 0
    else:
        occ = string.find(ch) #occ is occurrences
        if occ == -1:
            return 0 #if there is no result, return 0
        else:
            return (string[0]==ch)+count_letter(string[1:],ch) #else use recursion to count occurrences

#main
string = str(input("Enter a string: "))
ch = str(input("Enter a character: "))
print(count_letter(string,ch))

## Enter a string: Tha lattar A an thas santanca accars haw many tamas?
## Enter a character: a
## 14

