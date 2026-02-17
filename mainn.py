import os

# Save file in Android Downloads folder
FILE_NAME = "/storage/emulated/0/Download/students.txt"


def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                students.append({
                    "roll": roll,
                    "name": name,
                    "marks": marks
                })
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(f"{student['roll']},{student['name']},{student['marks']}\n")
    print("Data saved successfully.")
    print("File location:", FILE_NAME)


def add_student(students):
    roll = input("Enter Roll Number: ")

    # Check duplicate roll
    for student in students:
        if student["roll"] == roll:
            print("Error: Roll number already exists.")
            return

    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for student in students:
        print(f"Roll: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}")


def search_student(students):
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found:")
            print(f"Roll: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}")
            return

    print("Student not found.")


def delete_student(students):
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            save_students(students)
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()