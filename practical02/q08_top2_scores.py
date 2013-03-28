#filename: q08_top2_scores.py
#author: Yuan Siang
#created: 4/2/13
#modified: -
#description: Find the top 2 scores
#Practical 02 Q8

#main
#initialise new empty array
students = []

#initialise highest scores
highest = 0
highest2 = 0
highest_name = ""
highest_name2 = ""
#prompt for students
x = int(input("Enter number of students: "))

#ask for student details x times
for i in range (0, x):
    students.append([str(input("Enter student's name: ")), int(input("Enter student's score: "))])
#find the highest score
    if (students[i][1] > highest):
        highest = students[i][1]
        highest_name = students[i][0]
        top_num = i
#reset highest score to 0
students[top_num][1] = 0
#find second highest score
for i in range(0,x):
    if(students[i][1] > highest2):
        highest2 = students[i][1]
        highest_name2 = students[i][0]
#display results
print("Top student: " + highest_name + " and 2nd student: " + highest_name2 )
