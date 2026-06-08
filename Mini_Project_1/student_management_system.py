class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self):
        rollno = int(input("Enter Roll No: "))

        if rollno in self.students:
            print("Student already exists!")
            return

        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        self.students[rollno] = Student(rollno, name, marks)
        print("Student added successfully!")

    def search_student(self):
        roll = int(input("Enter Roll No to search: "))

        if roll in self.students:
            self.students[roll].display()
        else:
            print("Student not found!")

    def update_student(self):
        roll = int(input("Enter Roll No to update: "))

        if roll in self.students:
            name = input("Enter New Name: ")
            marks = float(input("Enter New Marks: "))

            self.students[roll].name = name
            self.students[roll].marks = marks

            print("Record updated successfully!")
        else:
            print("Student not found!")

    def delete_student(self):
        roll = int(input("Enter Roll No to delete: "))

        if roll in self.students:
            del self.students[roll]
            print("Record deleted successfully!")
        else:
            print("Student not found!")

    def display_all(self):
        if not self.students:
            print("No records found!")
        else:
            for student in self.students.values():
                print("\n")
                print("-"*15)
                student.display()


manager = StudentManager()

while True:
    print("\n----- Student Data Manager -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    match choice:
        case "1":
            manager.add_student()

        case "2":
            manager.search_student()

        case "3":
            manager.update_student()

        case "4":
            manager.delete_student()

        case "5":
            manager.display_all()

        case "6":
            print("Exiting...")
            break

        case _:
            print("Invalid choice!")