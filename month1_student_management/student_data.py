# Global list to store student records
students = []

# Function to add a new student to the list
def add_student():
    # Prompt user for student details
    name = input("Please enter your name: ")
    age = int(input("How old are you: "))
    grade = float(input("Please enter your grade: "))

    # Create a dictionary with the student's information
    student_info = {
        "student_name": name,
        "age": age,
        "grade": grade
    }

    # Add the student to the global students list
    students.append(student_info)

    # Return the newly added student info
    return student_info

# Function to display all students in the list
def view_students():
    # Loop through the list and print details for each student
    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}:")
        for key, value in student.items():
            print(f"  {key}: {value}")

# Function to calculate and return the average grade of all students
def get_average_grade():
    # If no students, return None to avoid division by zero
    if not students:
        return None

    # Sum up all grades
    total_grade = 0
    for student in students:
        total_grade += student["grade"]

    # Calculate average
    average_grade = total_grade / len(students)

    return average_grade
