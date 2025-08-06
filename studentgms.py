students = {}

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students[name] = grade
    print(f"Added {name} with grade {grade}")

def update_grade():
    name = input("Enter student name to update: ")
    if name in students:
        grade = float(input("Enter new grade: "))
        students[name] = grade
        print(f"Updated {name}'s grade to {grade}")
    else:
        print("Student not found")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        print(f"Removed student {name}")
    else:
        print("Student not found")

def average_grade():
    if students:
        avg = sum(students.values()) / len(students)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No students in the list")

def highest_and_lowest():
    if students:
        highest = max(students.values())
        lowest = min(students.values())
        # Find students with highest and lowest grades (optional)
        highest_students = [name for name, grade in students.items() if grade == highest]
        lowest_students = [name for name, grade in students.items() if grade == lowest]
        print(f"Highest grade: {highest} by {', '.join(highest_students)}")
        print(f"Lowest grade: {lowest} by {', '.join(lowest_students)}")
    else:
        print("No students in the list")

def list_students():
    if students:
        print("Students and grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("No students to show")

def main():
    while True:
        print("\nOptions:")
        print("1. Add student")
        print("2. Update student grade")
        print("3. Remove student")
        print("4. Show average grade")
        print("5. Show highest and lowest grades")
        print("6. List all students")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            average_grade()
        elif choice == "5":
            highest_and_lowest()
        elif choice == "6":
            list_students()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
