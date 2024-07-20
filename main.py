from College import CollegeManagement
from Department import Department
from Student import UGStudent
from Student import PGStudent
from Staff import *

def main_menu():
    while True:
        print("Welcome to the College Management System")
        print("Please select an option:")
        print("1. Open a College")
        print("2. View College Details")
        print("3. Manage Department")
        print("4. Student Affairs Administration")
        print("5. Staff administration")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            college_name = input("Enter the College Name: ")
            college = CollegeManagement()
            college.Open(college_name)
        elif choice == "2":
            college_id = input("Enter College ID: ")
            college = CollegeManagement()
            college.CollegeDetails(college_id)
        elif choice == "3":
            while True:
                department = Department()
                print("1. Add Department")
                print("2. View Department Details")
                print("3. Show events in a particular department")
                print("4. Go Back")
                choice = input("Enter your choice: ")
                if choice == "1":
                    depName = input("Enter Department Name:")
                    HOdName = input("Enter Head of the department name:")
                    total_staf = input("Enter TotalStaffs: ")
                    total_student = input("Enter TotalStudents: ")
                    department.addDepartment(depName,HOdName,total_staf,total_student)
                elif choice == "2":
                    dep = input("Enter Department ID: ")
                    department.DepartmentDetails(dep)
                elif choice == "3":
                    event = input("Enter Department ID: ")
                    department.ShowEvents(event)

                elif choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
         

        elif choice == "4":
            while True:
                UGstudent = UGStudent()
                PGstudent = PGStudent()
                print("1. Add Student")
                print("2. View Student Details")
                print("3. Payment status of each student")
                print("4. Is the student present")
                print("5. Go Back")
                option = input("Enter Your Choice: ")
                if option == "1":
                    college_id= input("Enter college ID:")
                    student_id = input("Enter Student ID:")
                    class_id = input("Enter Class ID: ")
                    name_student = input("Enter Student name: ")
                    gender_student = input("Enter Student gender: ")
                    year = input("Enter the year of enrollment: ")
                    payfees = input("Are college fees paid or not? [y/n]: ")
                    UGstudent.AddStudent(college_id,student_id,class_id,name_student,gender_student,year,payfees)
                elif option == "2":
                    select = input("1. Undergraduate Student\n2. Postgraduate Student\n Enter Your Choice: ")
                    if select == "1":
                        id_student = input("Enter Student ID: ")
                        UGstudent.StudentDetails(id_student)
                    elif select == "2":
                        id_student = input("Enter Student ID: ")
                        PGstudent.StudentDetails(id_student)
                elif option == "3":
                    UGStudent.PayFees(UGStudent)
                elif option == "4":
                    student_id = input("Enter Student ID:")
                    date = input("Enter Year: ")
                    UGStudent.IsPresent(UGStudent,student_id,date)
                elif option == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "5":
            teaching_staff_member = TeachingStaff()
            non_teaching_staff_member = NonTeachingStaff()
            while True:
                x = input("1. TeachingStaff Details\n2. NonTeachingStaff Details\n3. Go Back\nEnter Your Choice: ")
                if x == "1":
                    teaching_staff_member.StaffDetails()
                elif x == "2":
                    non_teaching_staff_member.StaffDetails()
                elif x == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
            
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