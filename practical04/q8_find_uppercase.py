#filename: q8_find_uppercase.py
#author: Yuan Siang
#created: 27/2/13
#modified: 1/3/13
#description: Find the number of uppercase letters in a string
#Practical 04 Q8

#define function find_num_uppercase(str)
def find_num_uppercase(string):
    if len(string)==1:
        if(65<=ord(string[0])<=90): #using the unicode values of the uppercase letters, check letter
            return 1 #case for when there is only 1 letter in string
        else:
            return 0
    else:
        if(65<=ord(string[0])<=90):
            return 1+find_num_uppercase(string[1:]) #use recursion to find no. of uppercaes letters in a large string
        else:
            return find_num_uppercase(string[1:])

#main
string = str(input("Enter a string: "))
print (find_num_uppercase(string))

## Enter a string: THERE are EXACTLY 13 uppercase letterS in this sentence
## 13