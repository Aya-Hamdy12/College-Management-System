from abc import ABC, abstractmethod
import json
import re

class CollegeManagement:
    def __init__(self,CollegeName,City,ContactNumber):
        self.__CollegeName = CollegeName
        self.__City = City
        self.__ContactNumber = ContactNumber

    def get_CollegeName(self):
        return self.__CollegeName
    def set_CollegeName(self,CollegeName):
        self.__CollegeName = CollegeName

    def get_City(self):
        return self.__City
    def set_City(self,City):
        self.__City = City

    def get_ContactNumber(self):
        return self.__ContactNumber
    def set_ContactNumber(self,ContactNumber):
        if type(ContactNumber) != (int):
            raise ValueError('Please enter vaild number')
        self.__ContactNumber = ContactNumber


    def Open(self):
        try:
            with open ("CollegeFile.txt","r") as CollegeFile:
                lines = CollegeFile.readlines()

        except FileNotFoundError:
            lines = []

        college_exists = False
        for line in lines:
            if self.get_CollegeName() in line:
                college_exists = True
                break

        with open("CollegeFile.txt","a") as CollegeFile:
            if not college_exists:
                print("This College does not exist.")
                option = input("Do you want to open this college? [y/n] ")
                if option.lower() == "y":
                    CollegeFile.write(f"College Name: {self.get_CollegeName()}\n")
                    CollegeFile.write(f"City: {self.get_City()}\n")
                    CollegeFile.write(f"Contact Number: {self.get_ContactNumber()}\n")
                    CollegeFile.write("-------------------------------------------\n")
                    CollegeFile.close()
                    print("The College is Open.\n")
            else:
                print("This College is open.")
               
                    
    def CollegeDetails(self):
        print(f"College Details\n CollegeName: {self.get_CollegeName()} \n City: {self.get_City()} \n ContactNumber: {self.get_ContactNumber()}")
        
        
class Department:
    static_var = 0
    def __init__(self,DepartmentId,DepartmentName,HODName,TotalStaffs,TotalStudents):
        Department.static_var += 1
        self.__DepartmentId = Department.static_var
        self._DepartmentName = DepartmentName
        self._HODName = HODName
        self.__TotalStaffs = TotalStaffs
        self.__TotalStudents = TotalStudents
    

    def get_DepartmentId(self):
        return self.__DepartmentId
    # def set_DepartmentId(self,DepartmentId):
    #     self.__DepartmentId = DepartmentId

    def get_DepartmentName(self):
        return self._DepartmentName
    def set_DepartmentName(self,DepartmentName):
        self._DepartmentName = DepartmentName

    def get_HODName(self):
        return self._HODName
    def set_HODName(self,HODName):
        self._HODName = HODName

    def get_TotalStaffs(self):
        return self.__TotalStaffs
    def set_TotalStaffs(self,TotalStaffs):
        self.__TotalStaffs = TotalStaffs

    def get_TotalStudents(self):
        return self.__TotalStudents
    def set_TotalStudents(self,TotalStudents):
        self.__TotalStudents = TotalStudents


    def DepartmentDetails(self):
        print(f"Department Details \n Department ID: {self.get_DepartmentId()} \n Department Name: {self.get_DepartmentName()} \n Name of department head: {self.get_HODName()} Total number of Staff : {self.get_TotalStaffs()} \n Total number of students: {self.get_TotalStudents()}")
        
    
    def ShowEvents(self,DepartmentID):
        try:
            with open ("Events.txt","r") as EventFile:
                lines = EventFile.readlines()

        except FileNotFoundError:
            lines = []

        event_exists = False
        for line in lines:
            if DepartmentID in line:
                event_exists = True
                break
        
        with open("Events.txt","a") as EventFile:
            if not event_exists:
                print("No events in this department.")
                option = input("Do you want to add event ? [y/n] ")
                if option.lower() == 'y':
                    EventFile.write(f"Department ID : {DepartmentID} \n Department Name: {self.get_DepartmentName()} \n")
                    date = input("Event Date : ")
                    EventFile.write(f"Event Date : {date} \n")
                    info = input("Event Details : ")
                    EventFile.write(f"Event Details : {info} \n")

            else:
                print(f"Department ID : {DepartmentID} \n Department Name: {self.get_DepartmentName()} \n Event Date : \n Event Details : \n")
                with open("Events.txt", "r") as EventFile:
                    data = EventFile.read()

                pattern = r"Department ID : (\d+)\n Department Name: (\w+)\n Event Date : (\d+/\d+/\d+)\n Event Details : (\w+)"
                matches = re.findall(pattern, data)
                
                for dept_id, dept_name, event_date, event_details in matches:
                    if int(dept_id) == DepartmentID:
                        print(f"Department ID: {DepartmentID} \n Department Name: {dept_name} \n Event Date:  {event_date} \n Event Details: {event_details}\n")
                        


class Classroom:
    def __init__(self, ClassId, Section, DepartmentId):
        self.ClassId = ClassId
        self.Section = Section
        self.DepartmentId = DepartmentId

    def ClassroomDetails(self):
        print("Class ID: ", self.ClassId)
        print("Section: ", self.Section)
        print("Department ID: ", self.DepartmentId)

    def IsOccupied(self):
        print("This method tells whether the classroom is occupied or not")



class Student:
    num_of_student = 0
    def __init__(self,StudentId,StudentName,Gender,Year,ClassId):
        Student.num_of_student += 1
        self.__StudentId = Student.num_of_student
        self.StudentName = StudentName
        self.__Gender = Gender
        self.__Year = Year
        self.__ClassId = ClassId

    def get_StudentId(self):
        return self.__StudentId
    def set_StudentId(self,StudentId):
        self.__StudentId = StudentId

    def get_StudentName(self):
        return self.StudentName
    def set_StudentName(self,StudentName):
        self.StudentName = StudentName

    def get_Gender(self):
        return self.__Gender
    def set_Gender(self,Gender):
        self.__Gender = Gender

    def get_Year(self):
        return self.__Year
    def set_Year(self,Year):
        self.__Year = Year

    def get_ClassId(self):
        return self.__ClassId
    # def set_ClassId(self,ClassId):
    #     self.__ClassId = ClassId

    def StudentDetails(self):
        try:
            with open ("StudentDetails.txt","r") as StudentFiles:
                lines = StudentFiles.readlines()

        except FileNotFoundError:
            lines = []

        Student_exists = False
        for line in lines:
            if self.get_StudentId() in line:
                Student_exists = True
                break

        with open("StudentDetails.txt","a") as StudentFiles:
            if not Student_exists:
                print("This Student does not exist in the College.")
                option = input("Do you want to add this Student in the college? [y/n] ")
                if option.lower() == "y":
                    StudentFiles.write(f"Student ID: {self.get_StudentId()}\n")
                    StudentFiles.write(f"Student Name: {self.get_StudentName()}\n")
                    StudentFiles.write(f"Gender: {self.get_Gender()}\n")
                    StudentFiles.write(f"Year of joining university: {self.get_Year()}\n")
                    StudentFiles.write(f"Class ID: {self.get_ClassId()}\n")
                    StudentFiles.write("-------------------------------------------\n")
                    StudentFiles.close()
                    print("The student has successfully enrolled in the university.\n")
            else:
                print(f"The Student Information \n Student ID: {self.get_StudentId()}\n Student Name: {self.get_StudentName()}\n Gender: {self.get_Gender()}\n Year of joining university: {self.get_Year()}\n Class ID: {self.get_ClassId()}\n")
    
    def PayFees(self,StudentID):
        print("This method contains the payment status of each student.")
        try:
            with open ("payFees.txt","r") as payFees_File:
                lines = payFees_File.readlines()
        except FileNotFoundError:
            lines = []

        payment_status = False
        for line in lines:
            if StudentID in line:
                payment_status = True
                break
        if not payment_status:
            print("This student did not pay the fees,")
            option = input("Do you want to pay now? [y/n] ")
            if option.lower() == "y":
                payFees_File.write(f"Student ID: {StudentID} \n")
                print("Payment completed successfully")

        else:
            print("This student has paid the fees")


    def IsPresent(self,StudentId,Date):
        with open("StudentDetails.txt","r") as StudentFiles:
            lines = StudentFiles.readlines()

        Student_is_present = False
        for line in lines:
            if StudentId and Date in line:
                Student_is_present = True
                break
        if not Student_is_present:
            print("The student is absent")

        else:
            print("The student is present")



class UGStudent(Student):
    def __init__(self, StudentId, StudentName, Gender, Year, ClassId):
        super().__init__(StudentId, StudentName, Gender, Year, ClassId)






class PGStudent(Student):
    def __init__(self, StudentId, StudentName, Gender, Year, ClassId):
        super().__init__(StudentId, StudentName, Gender, Year, ClassId)





# Abstraction
# abstractmethod Abstract Base Class
class Staff(ABC):
    StaffId_val = 0
    def __init__(self,StaffId,StaffName,Salary):
        Staff.StaffId_val += 1
        self.__StaffId = Staff.StaffId_val
        self.StaffName = StaffName
        self.Salary = Salary

    def get_StaffId(self):
        return self.__StaffId
    def get_DepartmentId(self):
        return self.__DepartmentId
    
    @abstractmethod
    def StaffDetails(self):
        pass
        
        


class TeachingStaff(Staff):
    def __init__(self, StaffId, StaffName, DepartmentId, Salary):
        super().__init__(StaffId, StaffName,Salary)
        self._DepartmentId = DepartmentId

    def StaffDetails(self):
        print("Staff ID: ", self.get_StaffId())
        print("Staff Name: ", self.StaffName)
        print("Department ID: ", self.get_DepartmentId())
        print("Salary : ", self.Salary)



class NonTeachingStaff(Staff):
    def __init__(self, StaffId, StaffName, Salary, Role):
        super().__init__(StaffId, StaffName,Salary)
        self._Role = Role


    def StaffDetails(self):
        print("Staff ID: ", self.get_StaffId())
        print("Staff Name: ", self.StaffName)
        print("Role: ", self._Role)
        print("Salary : ", self.Salary)


class Canteen:
    def __init__(self, InchargeId, ItemsList, AvailableList):
        self.InchargedId = InchargeId
        self.ItemsList = ItemsList
        self.AvailableList = AvailableList

    def ShowItems(self):
        print("Items which are present in the canteen: ", self.ItemsList)

    def Buy(self,Item):
        if Item in self.AvailableList:
            print(f"Bought {Item}.")
        else:
            print(f"{Item} is not available.")



# new_college = CollegeManagement("Helwan University", "Cairo", '01235485')
# new_college.Open()
# new_college.CollegeDetails()
# I promise I will do my best