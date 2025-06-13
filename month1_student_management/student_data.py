students = []

def add_student():
    name = input('Enter student name: ')
    age = int(input('Enter student age:  '))
    grade = float(input('Enter student grade: '))
    
    student = {
        'student_name' : name,
        'age' : age,
        'grade' : grade
    }

    students.append(student)
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    pass

def view_students():
    print('======Student Profiles=====')
    for student in students.items():
        print(f"Student name: {student['name']} \n Age: {student['age']} \n ")

    """    
    TODO: Loop through the students list and print each student's info.
    """
    pass

def get_average_grade():
   
   total_grade = sum(student['grade'] for student in students.item())
   avg_grade = total_grade/len(students)

    """
    TODO: Return the average grade of all students.
    """
    pass