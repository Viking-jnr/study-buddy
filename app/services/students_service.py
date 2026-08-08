from app.utils import display

def fetch_student(students, search_admission):
    for student in students:
        if student['admission_number'].lower() == search_admission.lower() or student['name'].lower() == search_admission.lower():
            return student
    return None

def add_student(students, student):
    students.append(student)
    return True

def search_student(students):
    if not students:
        print("No Students Found")
        return
    else:
        search_name = input("Enter student name or admission number: ").strip()
        found_students = []
        found_students.append(fetch_student(students, search_name))
        if found_students:
            display.view_student(found_students)
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
