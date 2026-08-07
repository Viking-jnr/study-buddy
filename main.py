
def display_menu():
    print("-----------------------")
    print("     STUDY BUDDY     ")
    print("-----------------------")
    print("\n\n1. Add Student\n2. View Student\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit\n\n")

def get_student_info():
    student_name = input("Enter student name: ").strip()
    admission_number = input("Enter admission number: ").strip()
    student_course = input("Enter student course: ").strip()
    return {
        "name": student_name,
        "admission_number": admission_number,
        "course": student_course
    }

def fetch_student(students, search_admission):
    for student in students:
        if student['admission_number'].lower() == search_admission.lower() or student['name'].lower() == search_admission.lower():
            return student
    return None

def add_student(students, student):
    students.append(student)

def view_student(students):
    if not students:
        print("No Students Found")
        return
    else:
        print("-------------Student List-------------")
        for index, student in enumerate(students, start = 1):
            print("========================================")
            print(f"Student {index}\n Name: {student['name']}\n Admission Number: {student['admission_number']}\n Course: {student['course']}")
            print("========================================")

def search_student(students):
    if not students:
        print("No Students Found")
        return
    else:
        search_name = input("Enter student name or admission number: ").strip()
        found_students = []
        found_students.append(fetch_student(students, search_name))
        if found_students:
            view_student(found_students)
        else:
            print(f"No students found with the info '{search_name}'.")

def update_student(students):
    search_admission = input("Enter the admission number of the student to update:  ").strip()
    found_student = fetch_student(students, search_admission)
    if found_student:
        print(f"Current Details\n Name: {found_student['name']}\n Admission Number: {found_student['admission_number']}\n Course: {found_student['course']}")
        print("Enter new details (leave blank to keep current values):")
        new_name = input("Enter new name: ").strip()
        new_course = input("Enter new course: ").strip()
        if new_name:
            found_student['name'] = new_name
        if new_course:
            found_student['course'] = new_course
        print("Student updated successfully!")
        print(f"Updated Details\n Name: {found_student['name']}\n Admission Number: {found_student['admission_number']}\n Course: {found_student['course']}")
        return

    # If student is not found
    print("Student not found")
    
    

def delete_student(students):
    search_admission = input("Enter the admission number of the student to delete: ").strip()
    found_student = fetch_student(students, search_admission)
    if found_student:
        print(f"Found Student\n Name: {found_student['name']}\n Admission Number: {found_student['admission_number']}\n Course: {found_student['course']}")
        confirmation = input("Are you sure? (Y/N): ")
        if confirmation.lower() == 'y':
            students.remove(found_student)
            print("Student deleted successfully")
            return
        elif confirmation.lower() == 'n':
            print("Deletion cancelled")
            return
        else: 
            print("Invalid Input. Enter 'Y' to confirm deletion or 'N' to cancel.")
            return
           
    
    print("Student not found")


students = []

choice = 0
while choice != 6:
    display_menu()
    choice = int(input("Choose an option: "))
    if choice == 6:
        print("Thank you for using study buddy. Goodbye!")
    elif choice == 1:
        student = get_student_info()
        add_student(students, student)
        print(f"Student {student['name']} added successfully!")
    elif choice == 2:
        view_student(students)
    elif choice == 3:
        search_student(students)
    elif choice == 4:
        update_student(students)
    elif choice == 5:
        delete_student(students)
    elif choice > 6 or choice < 1:
        print("Invalid option.\nPlease try again.")