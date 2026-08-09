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
            success = students_service.add_student(students, student)
            if success:
                print(f"Student {student['name']} added successfully!")
                storage_service.save_students(students)
        elif choice == 2:
            display.view_student(students)
        elif choice == 3:
            students_service.search_student(students)
        elif choice == 4:
            success = students_service.update_student(students)
            if success:
                storage_service.save_students(students)
        elif choice == 5:
            success = students_service.delete_student(students)
            if success:
                storage_service.save_students(students)

if __name__ == "__main__":
    main()