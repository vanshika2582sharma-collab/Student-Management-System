students=[]
while True:
    print("\n------Student Management System------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Exit")
     
    choice=int(input("Enter your choice: "))
    #Add Student
    if choice==1:
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        course=input("Enter your course: ")
        if name=="" or age=="" or course=="":
            print("All fields are required")
        else:
            student={
                "name": name,
                "age" : age,
                "course": course,
            }
            students.append(student)
            print("Student Added Successfully")
    # View Student
    elif choice==2:
        if len(students)==0:
            print("No Students found")  
        else:
            for s in students:
                print("---------------------")
                print("Name:",s["name"])
                print("Age:",s["age"])
                print("Course:",s["course"])
                print("---------------------")  
                print("Total Students:",len(students))
    # Deletee Student
    elif choice==3:
        name=input("Enter name to delete: ")
        found=False
        for s in students:
            if s["name"].lower()==name.lower():
                students.remove(s)      
                print("Student Deleted Successfully")
                found=True
                break
            if found==False:
                print("Student not found")
    # Exit 
    elif choice==4:
        print("Exiting Program....")
        break 
    else:
        print("Invalid choice")                           
