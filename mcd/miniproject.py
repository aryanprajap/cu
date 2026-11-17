# count the number of student 

numofstudent = int(input("enter totle students "))

#data storage
studentdata = []

#inserting data
for i in range(numofstudent):
    print("enter the no of student ",i+1)
    name = input("enter student name:")
    Roll_no = int(input("enter the rollno:"))
    marks = int(input("enter marks:"))

    if marks>90:
        Grade = "A"
    elif marks>80:
        Grade = "B"
    elif marks>70:
        Grade = "C"
    elif marks>60:
        Grade = "D"
    else:
        Grade = "F"
    
    students= {
        "name ": name,
        "Roll_no": Roll_no,
        "marks": marks,
        "Grade": Grade
    }

    studentdata.append(students)
    
    print ("all the students data : \n")
    for i in studentdata:
        print(i)
      
