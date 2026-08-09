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

def get_menu_choice():
    while True:
        try:
            choice = int(input("Choose an option: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_menu_choice():
    while True:
        choice = get_menu_choice()
        if 1 <= choice <= 6:
            return choice
        print("Invalid Option. Enter a valid option (1-6)")
        