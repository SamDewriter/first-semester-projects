students = []

def print_newline():
    """
    Print a newline for better readability.
    """
    print("--------------------------------------------------")
    print("\n")  # Print a newline for spacing
    pass

def add_student():
    """
    Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    print_newline()

    name = input("Enter student name: ").strip()

    if not name:
        print("  ⚠️  Name cannot be blank.")
        return
    try:
        age = int(input("Enter student age: ").strip())
        if age <= 0:
            print("  ⚠️  Age must be a positive integer.")
            return
    except ValueError:
        print("  ⚠️  Invalid age. Please enter a valid integer.")
        return
    
    try:
        grade = float(input("Enter student grade: ").strip())
        if grade < 0 or grade > 100:
            print("  ⚠️  Grade must be between 0 and 100.")
            return
    except ValueError:
        print("  ⚠️  Invalid grade. Please enter a valid number.")
        return  
    
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(student)
    print(f"✅ Student {name} added successfully.\n")
    print_newline()
    pass

def view_students():
    """
    Loop through the students list and print each student's info.
    """
    print_newline()
    if not students:
        print("📋 No students found.\n")
        return
    
    print("📋 List of Students: ")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']:.2f}")

    print_newline()
    pass

def get_average_grade():
    """
    Return the average grade of all students.
    """
    print_newline()
    if not students:
        print("📊 No students to calculate average grade.")
        return 0.0

    total_grade = sum(student['grade'] for student in students)
    print_newline()
    return total_grade / len(students)
    