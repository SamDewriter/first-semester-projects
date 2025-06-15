students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    grade = input("Enter student's grade: ")

    student_info = {
        "name": name,
        "age": int(age),
        "grade": int(grade)
    }

    students.append(student_info)
    print(students)
    pass

def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    for student in students:
        print(student)
    pass

def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    grades = []
    for student in students:
        print(student)
        grades.append(student["grade"])
    grade_average = sum(grades) / len(grades)
    return grade_average