# Initialize a global list to store all students
students = []

def add_student():
    """
    Adds students to the database until user enters 'stop'
    """
    print("\nAdd Student Mode (enter 'stop' as name to finish)")
    
    while True:
        print("\nPlease enter student information:")
        name = input("Name: ")
        
        if name.lower() == 'stop':
            print("\nStudent registration completed!")
            break
            
        age = input("Age: ")
        
        # Validate grade input
        while True:
            grade = input("Grade (0-100): ")
            try:
                grade = float(grade)
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100!")
            except ValueError:
                print("Please enter a valid number for grade!")
        
        # Add student to global list
        students.append({
            "name": name,
            "age": age,
            "grade": grade
        })
        
        print(f"\nStudent {name} added successfully!")
        print(f"Total students: {len(students)}")

def view_students():
    """
    Displays all students in the database
    """
    if not students:
        print("\nNo students in the database!")
        return
    
    print("\nSTUDENT DATABASE")
    print("=" * 40)
    for i, student in enumerate(students, 1):
        print(f"\nStudent #{i}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
    print("\n" + "=" * 40)
    print(f"Total students: {len(students)}")

def get_average_grade():
    """
    Calculates and returns the average grade
    """
    if not students:
        return 0.0
    
    total = sum(student['grade'] for student in students)
    return total / len(students)

def main_menu():
    """
    Main program interface
    """
    while True:
        print("\n" + "=" * 30)
        print("STUDENT MANAGEMENT SYSTEM")
        print("=" * 30)
        print("\n1. Add Students")
        print("2. View All Students")
        print("3. View Average Grade")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            avg = get_average_grade()
            print(f"\nAverage Grade: {avg:.2f}")
        elif choice == '4':
            print("\nThank you for using the system. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1-4")

if __name__ == "__main__":
    main_menu()