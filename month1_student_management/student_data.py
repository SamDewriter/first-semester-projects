students = []
grades = ['A', 'B', 'C', 'D', 'E', 'F']
gradeValues = {
    'A' : 5.00, 'B':4.00, 'C':3.00, 'D':2.00,'E':1.00,'F':0.00
}
# Prompt the user to enter student name, age, and grade.
# Append the student as a dictionary to the students list.
def add_student():
    name = input('Enter Student name: ').title()
    age = int(input ('Enter the age: '))
    while True:
        grade = input('Enter the grade (A-F): ').upper()
        if grade in grades:
            break
        print("Invalid grade, enter between A to F")

    student= {
        'name': name,
        'age' : age,
        'grade': grade
    }
    students.append(student)
    print(f"Student with details: '{name}', age '{age}' and grade '{grade}' added successfully!")
  

# Loop through the students list and print each student's info.
def view_students():
    if not students:
        print("Oops! Students list Empty")
    else:
        print("\n STUDENTS LIST ")  
        for index, student in enumerate(students, start = 1):
            print (f"{index}. {student} ")
    

 # Return the average grade of all students.
def get_average_grade():
    if not students:
        print('No students in the list to calculate average grade!\n')
    else:
        total = 0
        for student in students:
            total += gradeValues[student['grade']]
    
        average = total/len(students)
    #Converting to grade
        if average >= 4.50:
            averageGrade = 'A'
        elif average >= 3.50:
            averageGrade = 'B'
        elif average >= 3.00:
            averageGrade ='C'
        elif average >= 2.00:
            averageGrade ='D' 
        elif average >= 1.00:
            averageGrade ='E'
        else :
            averageGrade ='F' 
    print(f"\n Average letter Grade is:{averageGrade}")
    print(f"\n Average number Grade is:{average:.2f}")
