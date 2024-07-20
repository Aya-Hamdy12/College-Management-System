import json
import re
from abc import ABC, abstractmethod

class Department(ABC):
    __Dep_ID = 0
    
    def __init__(self, DepartmentName=None, HODName=None, TotalStaffs=None, TotalStudents=None):
        Department.__Dep_ID += 1
        self._DepartmentId = Department.__Dep_ID
        self._DepartmentName = DepartmentName
        self._HODName = HODName
        self._TotalStaffs = TotalStaffs
        self._TotalStudents = TotalStudents

    def get_DepartmentId(self):
        return self._DepartmentId

    def set_DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    def get_DepartmentName(self):
        return self._DepartmentName

    def set_DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName

    def get_HODName(self):
        return self._HODName

    def set_HODName(self, HODName):
        self._HODName = HODName

    def get_TotalStaffs(self):
        return self._TotalStaffs

    def set_TotalStaffs(self, TotalStaffs):
        self._TotalStaffs = TotalStaffs

    def get_TotalStudents(self):
        return self._TotalStudents

    def set_TotalStudents(self, TotalStudents):
        self._TotalStudents = TotalStudents

    def addDepartment(self, DepartmentName, HODName, TotalStaffs, TotalStudents):
        try:
            with open("DepartmentFile.txt", "a") as DepartmentFile:
                DepartmentFile.write(f"{Department.__Dep_ID}-")
                DepartmentFile.write(f"{DepartmentName}-")
                DepartmentFile.write(f"{HODName}-")
                DepartmentFile.write(f"{TotalStaffs}-")
                DepartmentFile.write(f"{TotalStudents}\n")
                print("Department added successfully.")
        except FileNotFoundError:
            print("Error: DepartmentFile.txt not found.")

    def DepartmentDetails(self, Department_ID):
        try:
            with open("DepartmentFile.txt", "r") as dep_file:
                lines = dep_file.readlines()  
        except FileNotFoundError:
            print("Department file not found.")
            return

        for line in lines:
            details = line.strip().split('-')
            if len(details) == 5:
                department_id = details[0]
                department_name = details[1]
                Hodname = details[2]
                total_staff = details[3]
                total_student = details[4]

            if Department_ID == department_id:
                print("Department Details\n")
                print(f"Department ID: {department_id}")
                print(f"Department Name: {department_name}")
                print(f"Name of Department Head: {Hodname}")
                print(f"Total Number of Staff: {total_staff}")
                print(f"Total Number of Students: {total_student}\n")
                break
            else:
                print(f"No department found with ID {Department_ID}\n")

    def ShowEvents(self, DepartmentID):
        try:
            with open("Events.txt", "r") as EventFile:
                lines = EventFile.readlines()
        except FileNotFoundError:
            lines = []

        event_found = False

        for line in lines:
            events = line.strip().split(',')
            if len(events) == 4:
                depEvent_id = events[0]
                depEvent_name = events[1]
                event_date = events[2]
                event_info = events[3]

            if DepartmentID == depEvent_id:
                print("Event Details\n")
                print(f"Department Name: {depEvent_name}")
                print(f"Event Date: {event_date}")
                print(f"Event Details: {event_info}\n")
                event_found = True

        if not event_found:
            option = input(f"No events found for Department ID {DepartmentID}. Do you want to add an event? [y/n] ")
            if option.lower() == 'y':
                try:
                    with open("Events.txt", "a") as EventFile:
                        EventFile.write(f"{DepartmentID},")
                        dep_name = input("Enter Department Name: ")
                        EventFile.write(f"{dep_name},")
                        event_date = input("Enter Event Date: ")
                        EventFile.write(f"{event_date},")
                        event_details = input("Enter Event Details: ")
                        EventFile.write(f"{event_details}\n")
                        print("Event added successfully.")
                except FileNotFoundError:
                    print("Error: Events.txt not found.")

                    
