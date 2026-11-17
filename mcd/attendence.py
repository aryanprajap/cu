no_of_students = int(input("enter the number of students"))

students=[]

for i in range (no_of_students):
    name=input("enter the name of student :")
    roll_no=int(input("enter the roll number of student :"))
    total_classes = int(input("enter the total number of classes :"))
    classes_attended = int(input("enter the number of classes attended:"))
    Attendence  = classes_attended /total_classes*100
    if Attendence>75:
        print("Allowed")
    else:
        print("short attendence")
    
    store = {
        "name":name,
        "roll_no":roll_no,
        "total_classes":total_classes,
        "classes_attended":classes_attended,
        "attendence %":Attendence     
    }
    students.append(store)

print("all the students data : \n")
for i in students:
    print(i)

   
    
        