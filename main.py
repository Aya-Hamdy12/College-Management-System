import json
class CollegeManagement:
    def __init__(self,CollegeName,City,ContactNumber):
        self.CollegeName = CollegeName
        self.City = City
        self.ContactNumber = ContactNumber

    def get_CollegeName(self):
        return self.CollegeName
    def set_CollegeName(self,CollegeName):
        self.CollegeName = CollegeName

    def get_City(self):
        return self.City
    def set_City(self,City):
        self.City = City

    def get_ContactNumber(self):
        return self.ContactNumber
    def set_City(self,ContactNumber):
        self.ContactNumber = ContactNumber


    def Open():
        return "The College is open."
    
    def CollegeDetails(self):
        return {
            "College Name: ": self.get_CollegeName,
            "City: ": self.get_City,
            "Contact Number: ": self.get_ContactNumber
        }
    



class Department:
    def __init__(self,DepartmentId,DepartmentName,HODName,TotalStaffs,TotalStudents):
        self.__DepartmentId = DepartmentId
        self.DepartmentName = DepartmentName
        self.HODName = HODName
        self._TotalStaffs = TotalStaffs
        self._TotalStudents = TotalStudents
    

    def get_DepartmentId(self):
        return self.__DepartmentId
    def set_DepartmentId(self,DepartmentId):
        self.__DepartmentId = DepartmentId

    def get_DepartmentName(self):
        return self.DepartmentName
    def set_DepartmentName(self,DepartmentName):
        self.DepartmentName = DepartmentName

    def get_HODName(self):
        return self.HODName
    def set_HODName(self,HODName):
        self.HODName = HODName

    def get_TotalStaffs(self):
        return self._TotalStaffs
    def set_TotalStaffs(self,TotalStaffs):
        self._TotalStaffs = TotalStaffs

    def get_TotalStudents(self):
        return self._TotalStudents
    def set_TotalStudents(self,TotalStudents):
        self._TotalStudents = TotalStudents


    def DepartmentDetails(self):
        return {
            "Department Name: ": self.get_DepartmentName,
            "Name of department head: ": self.get_HODName,
            "Total number of students: ": self.get_TotalStudents
        }
    
    def ShowEvents():
        return "No events in this department."
    

# I promise I will do my best 