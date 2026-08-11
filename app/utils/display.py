def view_student(students):
    if not students:
        print("No Students Found")
        return
    else:
        print("-------------Student List-------------")
        for index, student in enumerate(students, start = 1):
            print("========================================")
            print(f"Student {index}\n Name: {student['name']}\n Admission Number: {student['admission_number']}\n Course: {student['course']}")
            print("========================================")

def display_student(student):
    print("---------Found Student--------")
    print(f" Name: {student['name']}\n Admission Number: {student['admission_number']}\n Course: {student['course']}")

