students = []

while True:

    print("\n===================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)

        print("\nStudent Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("\nNo Students Found.")

        else:
            print("\nStudent List\n")

            for student in students:
                print("-------------------------")
                print("ID :", student["id"])
                print("Name :", student["name"])
                print("Age :", student["age"])
                print("Course :", student["course"])

    elif choice == "3":

        search = input("Enter Student ID: ")

        found = False

        for student in students:

            if student["id"] == search:

                print("\nStudent Found")
                print(student)

                found = True

                break

        if not found:
            print("Student Not Found")

    elif choice == "4":

        update_id = input("Enter Student ID to Update: ")

        found = False

        for student in students:

            if student["id"] == update_id:

                student["name"] = input("New Name: ")
                student["age"] = input("New Age: ")
                student["course"] = input("New Course: ")

                print("Student Updated Successfully")

                found = True

                break

        if not found:
            print("Student Not Found")

    elif choice == "5":

        delete_id = input("Enter Student ID to Delete: ")

        found = False

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                print("Student Deleted Successfully")

                found = True

                break

        if not found:
            print("Student Not Found")

    elif choice == "6":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")