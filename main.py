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
            search_choice = input_handler.get_valid_search_choice()
            if search_choice == 1:
                search_name = input_handler.get_student_name()
                search_option = 'name'
                
            elif search_choice == 2:
                search_name = input_handler.get_student_admission_number()
                search_option = 'admission'
            
            else:
                search_name = None
                search_option = 'cancel'
    
            success, result = students_service.search_student(students, search_name, search_option)
            if success:
                display.view_student(result)
            else:
                print(result)

        elif choice == 4:
            admission_number = input_handler.get_student_admission_number()
            found_student = students_service.fetch_with_admission(students, admission_number)
            if found_student:
                display.display_student(found_student)
                new_name, new_course = input_handler.get_new_details()
                success, result = students_service.update_student(found_student, new_name, new_course)
                if success:
                    print("Student updated successfully. Here's the updated student")
                    display.display_student(result)
                    storage_service.save_students(students)
                else:
                    print(result)
            else:
                print("Student not found")

        elif choice == 5:
            search_admission = input_handler.get_student_admission_number()
            found_student = students_service.fetch_with_admission(students, search_admission)
            if found_student:
                display.display_student(found_student)
                confirmation = input_handler.get_delete_confirmation()
                if confirmation == 'y':
                    success, error = students_service.delete_student(students, found_student)
                    if success:
                        print("Student deleted successfully")
                        storage_service.save_students(students)
                    else: 
                        print(error)
                else:
                    print("Deletion Cancelled")
           
            
            else:
                print("Student not found")

if __name__ == "__main__":
    main()