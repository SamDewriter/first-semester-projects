students = []
def add_student():
    while True:
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        student = {"name": name, "marks":marks}
        students.append(student)
        print(f"{name} has been added.\n")
        another = input("Do you want to add another student? (yes/no): ").strip().lower()
        if another != "yes":
            break
def view_students():
    if len(students) == 0:
        print("No students to display.\n")
    else:
        print("Student List:")
        for student in students:
            print(f"Name: {student['name']}, marks: {student['marks']}")
        print()
def get_average_marks():
    if len(students) == 0:
        print("No students to calculate average grade.\n")
        return 0
    total_marks = sum(student['marks'] for student in students)
    average_marks = total_marks / len(students)
    return average_marks
def convert_marks_to_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 85:
        return "A-"
    elif mark >= 80:
        return "B+"
    elif mark >= 75:
        return "B"
    elif mark >= 70:
        return "B-"
    elif mark >= 65:
        return "C+"
    elif mark >= 60:
        return "C"
    elif mark >= 55:
        return "C-"
    elif mark >= 50:
        return "D+"
    elif mark >= 45:
        return "D"
    elif mark >= 40:
        return "D-"
    else:
        return "F"  
def show_class_statistics():
    if len(students) == 0:
        print("No students to show statistics.\n")
        return
    average = get_average_marks()
    average_grade = convert_marks_to_grade(average)
    print("=== Class Statistics ===")
    print(f"Total Students: {len(students)}")
    print(f"Average Marks: {average:.2f} (Grade: {average_grade})")
def main():
    print("Welcome to Student Data Management System!")
    while True:
        print("\nMenu Options:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Show Class Statistics")
        print("4. Exit")
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                show_class_statistics()
            elif choice == "4":
                print("Thank you for using Student Data Management System!")
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.\n")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()    


            