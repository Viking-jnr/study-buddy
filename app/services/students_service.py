from app.utils import validators

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
    return None

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

def search_student(students, search_term, search_option):
    if not students:
        return False, "No Students Found"
    
    if search_option == 'name':
        found_students = fetch_with_name(students, search_term)
        if found_students:
            return True, found_students
    elif search_option == 'admission':
        found_students = fetch_with_admission(students, search_term)
        if found_students:
            return True, [found_students]
    else:
        return False, "Search Cancelled"
    
    return False, f"No students found with the info '{search_term}'"




def update_student(found_student, new_name, new_course):
    if not found_student:
        return False, "Student not found"
    if not new_name and not new_course:
        return False, "No changes were provided"

    if new_name:
        is_valid, error = validators.validate_student_name(new_name)
        if not is_valid:
            return False, error
    if new_course:
        is_valid, error = validators.validate_course(new_course)
        if not is_valid:
            return False, error

    if new_name:
        found_student['name'] = new_name
    if new_course:
        found_student['course'] = new_course

    return True, found_student

    
    

def delete_student(students, found_student):
    if found_student:
        students.remove(found_student)
        return True, None
    return False, "Student not found"
           

def validate_admission_number(admission_number, students):
    found_student = fetch_with_admission(students, admission_number)
    if found_student:
        return False, "Admission number already exists."
    return True, None

