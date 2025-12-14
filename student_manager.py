import csv
import os

# File to store student data
FILE_NAME = "students.csv"
FIELDS = ["id", "name", "course", "email"]

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)

def load_students():
    """Reads all students from the CSV into a list of dictionaries."""
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students

def save_students(students):
    """Writes the list of students back to the CSV file."""
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)

def add_student():
    """Adds a new student after validating that the ID is unique."""
    students = load_students()
    
    print("\n--- Add New Student ---")
    try:
        student_id = input("Enter Student ID: ").strip()
        if not student_id.isdigit():
            print("❌ Error: ID must be numeric.")
            return

        # Check for Duplicate ID
        for s in students:
            if s['id'] == student_id:
                print("❌ Error: Student ID already exists!")
                return

        name = input("Enter Name: ").strip()
        if not name:
            print("❌ Error: Name cannot be empty.")
            return

        course = input("Enter Course: ").strip()
        email = input("Enter Email: ").strip()
        if "@" not in email:
             print("❌ Warning: Invalid email format.")
        
        # Add to list and save
        new_student = {"id": student_id, "name": name, "course": course, "email": email}
        students.append(new_student)
        save_students(students)
        print("✅ Student added successfully!")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

def search_student():
    """Searches for a student by ID."""
    search_id = input("\nEnter Student ID to Search: ").strip()
    students = load_students()
    found = False
    
    for s in students:
        if s['id'] == search_id:
            print(f"\n🔍 Student Found:")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Course: {s['course']}")
            print(f"Email: {s['email']}")
            found = True
            break
    
    if not found:
        print("❌ Student not found.")

def view_all_students():
    """Displays all students in a table format."""
    students = load_students()
    if not students:
        print("\n📂 No records found.")
        return

    print("\n📋 List of All Students")
    print("-" * 60)
    print(f"{'ID':<10} {'Name':<20} {'Course':<10} {'Email':<20}")
    print("-" * 60)
    for s in students:
        print(f"{s['id']:<10} {s['name']:<20} {s['course']:<10} {s['email']:<20}")
    print("-" * 60)

def delete_student():
    """Deletes a student by ID."""
    delete_id = input("\nEnter Student ID to Delete: ").strip()
    students = load_students()
    new_students = [s for s in students if s['id'] != delete_id]

    if len(students) == len(new_students):
        print("❌ Student ID not found.")
    else:
        save_students(new_students)
        print("✅ Student deleted successfully!")

def main():
    """Main menu loop matching the Flowchart."""
    initialize_file()
    
    while True:
        print("\n--- 🎓 Student Management System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
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
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()