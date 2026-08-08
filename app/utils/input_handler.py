def get_student_info():
    student_name = input("Enter student name: ").strip()
    admission_number = input("Enter admission number: ").strip()
    student_course = input("Enter student course: ").strip()
    if student_name and admission_number and student_course:
        return {
            "name": student_name,
            "admission_number": admission_number,
            "course": student_course
        }
    return None