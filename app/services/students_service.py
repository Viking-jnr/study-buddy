from app.utils import display, validators, input_handler
from app import menu

def fetch_with_name(students, search_name):
    found_students = []
    for student in students:
        if search_name.lower() in student['name'].lower():
            found_students.append(student)
    return found_students

def fetch_with_admission(students, search_admission):
    for student in students:
        if student['admission_number'].lower() == search_admission.lower():
            return student
    return []

def add_student(students, student):
    is_valid, error = validators.validate_student_name(student['name'])
    if not is_valid:
            return False, error
    is_valid, error = validators.validate_course(student['course'])
    if not is_valid:
            return False, error
    is_valid, error = validate_admission_number(student['admission_number'], students)
    if not is_valid:
        return False, error
    students.append(student)
    return True, None

def search_student(students):
    if not students:
        return False, "No Students Found"
    else:
        choice = input_handler.get_valid_search_choice()
        if choice == 1:
            search_name = input_handler.get_student_name()
            found_students = fetch_with_name(students, search_name)
            if found_students:
                display.view_student(found_students)
                return True, None
        elif choice == 2:
            search_name = input_handler.get_student_admission_number()
            found_students = fetch_with_admission(students, search_name)
            if found_students:
                display.display_student(found_students)
                return True, None
        else:
            return False, "Search Cancelled"
        
        return False, f"No students found with the info '{search_name}'"




def update_student(students, admission_number, new_name, new_course):
    found_student = fetch_with_admission(students, admission_number)
    if found_student:
        display.display_student(found_student)
        if new_name:
            found_student['name'] = new_name
        if new_course:
            found_student['course'] = new_course
        return True, f"Updated Details\n Name: {found_student['name']}\n Admission Number: {found_student['admission_number']}\n Course: {found_student['course']}"

    # If student is not found
    return False, "Student not Found"
    
    

def delete_student(students):
    search_admission = input_handler.get_student_admission_number()
    found_student = fetch_with_admission(students, search_admission)
    if found_student:
        display.display_student(found_student)
        confirmation = input_handler.get_delete_confirmation()
        if confirmation == 'y':
            students.remove(found_student)
            return True, None
        else:
            return False, "Deletion Cancelled"
           
    return False,"student not found"

def validate_admission_number(admission_number, students):
    found_student = fetch_with_admission(students, admission_number)
    if found_student:
        return False, "Admission number already exists."
    return True, None

