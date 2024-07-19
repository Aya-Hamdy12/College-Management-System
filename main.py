from CollegeManagement import CollegeManagement
from Department import Department
def main_menu():
    while True:
        print("Welcome to the College Management System")
        print("Please select an option:")
        print("1. Open a College")
        print("2. View College Details")
        print("3. Manage Department")
        print("4. View Department Details")
        print("5. Show events in a particular department")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            college_name = input("Enter the College Name: ")
            college_city = input("Enter the City: ")
            college_contact = int(input("Enter the Contact Number: "))
            college = CollegeManagement(college_name, college_city, college_contact)
            college.Open()
        elif choice == "2":
            college_name = input("Enter the College Name: ")
            # college_city = input("Enter the City: ")
            # college_contact = int(input("Enter the Contact Number: "))
            college = CollegeManagement(college_name)
            college.CollegeDetails(college_name)
        elif choice == "3":
            print("1. Add Department:")
            print("2. View Department Details")
            print("3. Show events in a particular department")
            print("4. Go Back")
            choice = input("Enter your choice: ")
            if choice == "1":
                depID = input("Enter Department ID: ")
                depName = input("Enter Department Name:")
                HOdName = input("Enter Head of the department name:")
                total_staf = input("Enter TotalStaffs: ")
                total_student = input("Enter TotalStudents: ")
                department = Department(depID,depName,HOdName,total_staf,total_student)
                department.addDepartment(depID,depName,HOdName,total_staf,total_student)
            elif choice == "2":
                dep = input("Enter Department ID: ")
                department.DepartmentDetails()
                pass

            elif choice == "3":
                pass

            elif choice == "4":
                pass
         

        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("Exiting the College Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()
# new_college = CollegeManagement("Helwan University", "Cairo", '01235485')
# new_college.Open()
# new_college.CollegeDetails()
# I promise I will do my best