

def validate_student_name(name):
    if name.strip() == "":
        return False, "Student name cannot be empty."
    
    if len(name) < 2:
        return False, "Student name must be at least 2 characters long."

    if not all(word.isalpha() for word in name.split()):
        return False, "Student name must only contain alphabetic characters and spaces"
    

    return True, None

def validate_course(course):
    if course.strip() == "":
        return False, "Student course cannot be empty."
    elif len(course) < 2:
        return False, "Student course must be at least 2 characters long."
    else:
        return True, None