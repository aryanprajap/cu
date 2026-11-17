numofrecords = int(input("enter number of records : "))

students = []

for i in range (numofrecords):
    name=input("enter the name of student :")
    roll_no=int(input("enter the roll number of student :"))
    english = int(input("enter marks in english : "))
    maths = int(input("enter marks in maths : "))
    science = int(input("enter marks in science : "))
    computer_marks= int(input("enter marks in computer :"))

Total_marks = english + maths + science + computer_marks
Percentage = (Total_marks/400)*100

pass_mark = 132

if Percentage >=90:
    print("Grade = A")
elif Percentage >=80:
    print("Grade = B")
elif Percentage >=70:
    print("Grade = C")
elif Percentage >=60:
    print("Grade = D")
else:
    print("Grade = F")

if Total_marks>=132:
    print("pass")
else:
    print("fail")
    
student_data = {
    "name" : name,
    "roll_no" : roll_no,
    "english" : english,
    "maths" : maths,
    "science" : science,
    "computer_marks" : computer_marks,
    "total_marks" : Total_marks,
    "Percentage": Percentage,
    "pass": pass_mark
}

students.append(student_data)


highest_percentage = 0
highest_student = None

for students in student_data:
    if Percentage > highest_percentage:
        highest_percentage = Percentage
        highest_student = name

print("Highest percentage:", highest_percentage) 
print("Student:", name)
