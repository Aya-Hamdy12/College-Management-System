import CollegeManagement
import json
import re
from abc import ABC, abstractmethod

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
