from app import menu
from app.utils import input_handler, display
from app.services import students_service


def main():
    students = []
    choice = 0
    while choice != 6:
        menu.display_menu()
        choice = int(input("Choose an option: "))
        if choice == 6:
            print("Thank you for using study buddy. Goodbye!")
        elif choice == 1:
            student = input_handler.get_student_info()
            success = students_service.add_student(students, student)
            if success:
                print(f"Student {student['name']} added successfully!")
        elif choice == 2:
            display.view_student(students)
        elif choice == 3:
            students_service.search_student(students)
        elif choice == 4:
            students_service.update_student(students)
        elif choice == 5:
            students_service.delete_student(students)
        elif choice > 6 or choice < 1:
            print("Invalid option.\nPlease try again.")

if __name__ == "__main__":
    main()