from app import menu
from app.utils import input_handler, display
from app.services import students_service, storage_service


def main():
    students = storage_service.load_students()
    choice = 0
    while choice != 6:
        menu.display_menu()
        choice = input_handler.get_valid_menu_choice()
        if choice == 6:
            print("Thank you for using study buddy. Goodbye!")
        elif choice == 1:
            student = input_handler.get_student_info()
            success, error = students_service.add_student(students, student)
            if success:
                print(f"Student {student['name']} added successfully!")
                storage_service.save_students(students)
            else:
                print(error)
        elif choice == 2:
            display.view_student(students)
        elif choice == 3:
            menu.display_search_menu()
            success, error = students_service.search_student(students)
            if not success:
                print(error)
        elif choice == 4:
            admission_number = input_handler.get_student_admission_number()
            new_name, new_course = input_handler.get_new_details()
            success, error = students_service.update_student(students, admission_number, new_name, new_course)
            if success:
                print("Student updated successfully")
                print(error)
                storage_service.save_students(students)
            else:
                print(error)
        elif choice == 5:
            success, error = students_service.delete_student(students)
            if success:
                print("Student deleted successfully")
                storage_service.save_students(students)
            else:
                print(error)

if __name__ == "__main__":
    main()