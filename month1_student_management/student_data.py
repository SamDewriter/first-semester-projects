students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))
    
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)

def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    if not students:
        print("No students found.")
        return
    
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    if not students:
        return 0
    
    total_grade = sum(student['grade'] for student in students)
    return total_grade / len(students)