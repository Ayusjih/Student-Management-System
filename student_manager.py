
import csv
import os

# Configuration: File to store student data
FILE_NAME = "students.csv"
FIELDS = ["id", "name", "course", "email"]

def initialize_file():
    """
    Checks if the CSV file exists. If not, creates it with the header row.
    Requirement: If file does not exist -> create automatically.
    """
    if not os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(FIELDS)
        except IOError as e:
            print(f"❌ Error creating file: {e}")

def load_students():
    """Reads all student records from CSV into a list of dictionaries."""
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students

def save_students(students):
    """Overwrites the CSV file with the current list of students."""
    try:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)
    except IOError as e:
        print(f"❌ Error saving data: {e}")

def add_student():
    """
    Adds a new student.
    Validations: Unique ID, Numeric ID, Non-empty Name, Valid Email.
    """
    print("\n--- ➕ Add New Student ---")
    students = load_students()
    
    # 1. Validate ID
    student_id = input("Enter Student ID: ").strip()
    if not student_id.isdigit():
        print("❌ Error: ID must be numeric.")
        return
    
    # Check for duplicate ID
    for s in students:
        if s['id'] == student_id:
            print(f"❌ Error: Student ID {student_id} already exists.")
            return

    # 2. Validate Name
    name = input("Enter Name: ").strip()
    if not name:
        print("❌ Error: Name cannot be empty.")
        return

    # 3. Input Course
    course = input("Enter Course: ").strip()

    # 4. Validate Email
    email = input("Enter Email: ").strip()
    if "@" not in email:
        print("❌ Error: Invalid email format (must contain '@').")
        return

    # Append new student
    new_student = {"id": student_id, "name": name, "course": course, "email": email}
    students.append(new_student)
    save_students(students)
    print("✅ Student added successfully!")

def search_student():
    """Searches for a student by ID and displays details."""
    print("\n--- 🔍 Search Student ---")
    search_id = input("Enter Student ID to Search: ").strip()
    students = load_students()
    
    found = False
    for s in students:
        if s['id'] == search_id:
            print("\n🎓 Student Details Found:")
            print(f"ID     : {s['id']}")
            print(f"Name   : {s['name']}")
            print(f"Course : {s['course']}")
            print(f"Email  : {s['email']}")
            found = True
            break
    
    if not found:
        print("❌ Student not found.")

def delete_student():
    """Deletes a student record by ID."""
    print("\n--- 🗑️ Delete Student ---")
    delete_id = input("Enter Student ID to Delete: ").strip()
    students = load_students()
    
    # Filter out the student with the matching ID
    new_list = [s for s in students if s['id'] != delete_id]
    
    if len(students) == len(new_list):
        print("❌ Error: Student ID not found.")
    else:
        save_students(new_list)
        print(f"✅ Student {delete_id} deleted successfully.")

def view_all_students():
    """Displays all students in a formatted table."""
    print("\n--- 📋 View All Students ---")
    students = load_students()
    
    if not students:
        print("📂 No records found.")
        return

    # Header
    print(f"{'ID':<10} {'Name':<20} {'Course':<10} {'Email':<25}")
    print("-" * 65)
    
    # Rows
    for s in students:
        print(f"{s['id']:<10} {s['name']:<20} {s['course']:<10} {s['email']:<25}")
    print("-" * 65)

def main():
    """Main Menu Loop."""
    initialize_file()
    
    while True:
        print("\n=== 🎓 Student Management System ===")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            view_all_students()
        elif choice == '5':
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
