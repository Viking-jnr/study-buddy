def get_student_info():
    student_name = get_required_input("Enter student name: ")
    admission_number = get_required_input("Enter admission number: ")
    student_course = get_required_input("Enter student course: ")
    
    return {
            "name": student_name,
            "admission_number": admission_number,
            "course": student_course
        }

def get_required_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty")

    
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

def get_valid_search_choice():
    while True:
        choice = get_menu_choice()
        if 1 <= choice <= 3:
            return choice
        print("Invalid Option. Enter a valid option (1 - 3)")


def get_student_admission_number():
    admission_number = get_required_input("Enter the admission number of the student: ")
    return admission_number 

def get_student_name():
    name = get_required_input("Enter the name of the student: ")  
    return name 


def get_delete_confirmation():
    while True:
        confirmation = get_required_input("Are you sure (Y/N): ")
        if confirmation.lower() in ['y', 'n' ]:
            return confirmation.lower()
        print("Invalid Input. Enter 'Y' to confirm deletion or 'N' to cancel.")

def get_new_details():
    print("Enter new details (leave blank to keep current values):")
    
    new_name = input("Enter new name: ").strip()
    new_course = input("Enter new course: ").strip()
    return new_name, new_course
