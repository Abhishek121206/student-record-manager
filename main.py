import csv

def read_students():
    with open("students.csv",'r') as file:
        reader= csv.DictReader(file)

        students=[]

        for row in reader:
            students.append(row)

        return students

def display_students(students):
    for student in students:
        print(
            f"Id: {student['ID']} | "
            f"Name: {student['Name']} | "
            f"Marks: {student['Marks']}"
        )

def calculate_average(students):
    if len(students) == 0:
        return 0
    
    total=0

    for student in students:
        total+=int((student['Marks']))
    return total/len(students)

def find_highest_scorer(students):
    highest=''
    maxm=0
    for student in students:
        if int(student['Marks'])>maxm:
            maxm=int(student['Marks'])
            highest=student['Name']
    return highest

def add_student(students):
    student_ID = input("Enter student ID: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    student = {
        "ID": student_ID,
        "Name": name,
        "Marks": marks
    }
    students.append(student)
    return students

def save_students(students):
    with open("students.csv",'w',newline="") as file:
        fieldnames=["ID","Name","Marks"]

        writer=csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

def update_student(students):
    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["ID"]== student_id:
            new_name = input("Enter updated Name: ")
            new_marks = input("Enter updated Marks: ")

            student["Name"]=new_name
            student["Marks"]=new_marks
            print("Student updated successfully!")
            return students

    print("Student not found!")
    return students

def delete_student(students):
    student_id= input("Enter ID of student to delete: ")

    for student in students:
        if student["ID"]== student_id:
            students.remove(student)
            print("Student removed successfully")
            return students

    print("Student not found")
    return students

if __name__ == "__main__":
    students = read_students()

    while True:
        print("\n====== Student Record Manager ======")
        print("1. Display students")
        print("2. Add student")
        print("3. Update student")
        print("4. Delete student")
        print("5. Calculate average")
        print("6. Find highest scorer")
        print("7. Exit")

        choice = input("Enter choice of func to perform: ")

        match choice: 
            case "1":
                display_students(students)
            case "2":
                students = add_student(students)
                save_students(students)
            case "3":
                students = update_student(students)
                save_students(students)
            case "4":
                students=delete_student(students)
                save_students(students)
            case "5":
                print("Average Marks:", calculate_average(students))
            case "6":
                print("Highest Scorer:", find_highest_scorer(students))
            case "7":
                print("Exiting...")
                break
            case _:
                print("Invalid Choice")



