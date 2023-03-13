# Define an empty list to store student records
students = []

# Define a function to add a new student record
def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)

# Define a function to display all student records
def display_students():
    print("Student records:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Define a function to search for a student by name
def search_student():
    name = input("Enter student name: ")
    for student in students:
        if student["name"] == name:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            return
    print("Student not found.")

# Define a function to delete a student record
def delete_student():
    name = input("Enter student name: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student record deleted.")
            return
    print("Student not found.")

# Main program loop
while True:
    print("\nStudent Management System")
    print("1. Add student record")
    print("2. Display all student records")
    print("3. Search for a student")
    print("4. Delete a student record")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
