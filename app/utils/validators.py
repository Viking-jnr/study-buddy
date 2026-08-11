

def validate_student_name(name):
    if name.strip() == "":
        return False, "Student name cannot be empty."
    elif len(name) < 2:
        return False, "Student name must be at least 2 characters long."
    else:
        return True, None

def validate_course(course):
    if course.strip() == "":
        return False, "Student course cannot be empty."
    elif len(course) < 2:
        return False, "Student course must be at least 2 characters long."
    else:
        return True, None