import json
import re
from abc import ABC, abstractmethod
from CollegeManagement import CollegeManagement
class Department(ABC):

    def __init__(self,DepartmentId, DepartmentName, HODName, TotalStaffs, TotalStudents):
        self.__DepartmentId = DepartmentId
        self._DepartmentName = DepartmentName
        self._HODName = HODName
        self.__TotalStaffs = TotalStaffs
        self.__TotalStudents = TotalStudents

    def addDepartment(self,DepartmentId,DepartmentName,HODName,TotalStaffs,TotalStudents):
        try:
            with open ("DepartmentFile.txt","r") as DepartmentFile:
                lines = DepartmentFile.readlines()
        except FileNotFoundError:
            lines = []
        
        Department_exists = False
        for line in lines:
            if DepartmentName in line:
                Department_exists = True
                break

        with open("DepartmentFile.txt","a") as DepartmentFile:
            if not Department_exists:
                DepartmentFile.write(f"DepartmentId: {DepartmentId}\n")
                DepartmentFile.write(f"DepartmentName: {DepartmentName}\n")
                DepartmentFile.write(f"Head of the department name: {HODName}\n")
                DepartmentFile.write(f"TotalStaffs: {TotalStaffs}\n")
                DepartmentFile.write(f"TotalStudents: {TotalStudents}\n")
                print("Department add Successfly.")
            else:
                print("Department already exist.")


    

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
                with open("Events.txt", "r") as EventFile:
                    data = EventFile.read()

                pattern = r"Department ID : (\d+)\n Department Name: (\w+)\n Event Date : (\d+/\d+/\d+)\n Event Details : (\w+)"
                matches = re.findall(pattern, data)
                
                for dept_id, dept_name, event_date, event_details in matches:
                    if int(dept_id) == DepartmentID:
                        print(f"Department ID: {DepartmentID} \n Department Name: {dept_name} \n Event Date:  {event_date} \n Event Details: {event_details}\n")
                        

