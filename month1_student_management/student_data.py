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

    
    # TODO: Prompt the user to enter student name, age, and grade.
    # Append the student as a dictionary to the students list.
    
def view_students():
    print('======Student Profiles=====')
    for student in students:
        print(f"Student name: {student['name']} \n Age: {student['age']} \n grade: {student['grade']}")

    
    # TODO: Loop through the students list and print each student's info.
    


def get_average_grade():
   total_grade = sum(student['grade'] for student in students)
   avg_grade = total_grade/len(students)


    # TODO: Return the average grade of all students.