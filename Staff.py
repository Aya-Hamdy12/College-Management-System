import College
import json
import re
from abc import ABC, abstractmethod

teaching_Staff = [
    ['1001', 'John Doe', 'Computer Science', 60000],
    ['1002', 'Jane Smith', 'Computer Science', 65000],
    ['1003', 'Michael Johnson', 'Mathematics', 55000],
    ['1004', 'Emily Davis', 'English', 70000],
    ['1005', 'David Lee', 'Physics', 62000],
    ['1006', 'Sarah Lee', 'Chemistry', 68000],
    ['1007', 'Ethan Chen', 'Electrical Engineering', 72000],
    ['1008', 'Olivia Patel', 'Mechanical Engineering', 75000],
    ['1009', 'Liam Nguyen', 'Civil Engineering', 63000],
    ['1010', 'Ava Gonzalez', 'Biology', 66000]
]

NonTeaching_Staff = [
    ['2001', 'Sarah Wilson', 45000, 'Administrative Assistant'],
    ['2002', 'Robert Chen', 50000, 'IT Support'],
    ['2003', 'Samantha Patel', 48000, 'Facilities Coordinator'],
    ['2004', 'Mark Goldstein', 52000, 'HR Specialist'],
    ['2005', 'Jessica Nguyen', 47000, 'Marketing Coordinator'],
    ['2006', 'Daniel Kim', 55000, 'Accounting Specialist'],
    ['2007', 'Sophia Ramirez', 49000, 'Events Coordinator'],
    ['2008', 'William Tanaka', 53000, 'Procurement Analyst'],
    ['2009', 'Isabella Kowalski', 51000, 'Facilities Technician'],
    ['2010', 'Jacob Hernandez', 46000, 'Administrative Coordinator']
]

# Abstraction
# abstractmethod Abstract Base Class
class Staff(ABC):
    StaffId_val = 0
    def __init__(self, StaffName=None, Salary=None):
        Staff.StaffId_val += 1
        self.__StaffId = Staff.StaffId_val
        self.StaffName = StaffName
        self.Salary = Salary

    def get_StaffId(self):
        return self.__StaffId
    
    @abstractmethod
    def StaffDetails(self):
        pass

class TeachingStaff(Staff):
    def __init__(self, StaffName=None, Salary=None, DepartmentName=None):
        super().__init__(StaffName, Salary)
        self.DepartmentName = DepartmentName

    def StaffDetails(self):
        print("Teaching Staff Details:")
        for staff in teaching_Staff:
            staff_id, staff_name, department_name, salary = staff
            print(f"Staff ID: {staff_id}")
            print(f"Staff Name: {staff_name}")
            print(f"Department Name: {department_name}")
            print(f"Salary: {salary}")
            print()

class NonTeachingStaff(Staff):
    def __init__(self, StaffName=None, Salary=None, Role=None):
        super().__init__(StaffName, Salary)
        self.Role = Role

    def StaffDetails(self):
        print("Non-Teaching Staff Details:")
        for staff in NonTeaching_Staff:
            staff_id, staff_name, salary, role = staff
            print(f"Staff ID: {staff_id}")
            print(f"Staff Name: {staff_name}")
            print(f"Role: {role}")
            print(f"Salary: {salary}")
            print()
