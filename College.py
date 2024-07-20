import json
import re
from abc import ABC, abstractmethod


class CollegeManagement:
    __CollegeID = 0
    def __init__(self, CollegeName = None, City = None, ContactNumber = None):
        CollegeManagement.__CollegeID += 1
        self.__ID = CollegeManagement.__CollegeID
        self.__CollegeName = CollegeName
        self.__City = City
        self.__ContactNumber = ContactNumber


    def set_CollegeName(self,CollegeName):
        self.__CollegeName = CollegeName
    def get_CollegeName(self):
        return self.__CollegeName
    
    def set_City(self,City):
        self.__City = City
    def get_City(self):
        return self.__City
    
    def set_ContactNumber(self,ContactNumber):
        if type(ContactNumber) != (int):
            raise ValueError('Please enter vaild number')
        self.__ContactNumber = ContactNumber
    def get_ContactNumber(self):
        return self.__ContactNumber


    def Open(self,CollegeName):
        try:
            with open ("CollegeFile.txt","r") as CollegeFile:
                lines = CollegeFile.readlines()

        except FileNotFoundError:
            lines = []

        college_exists = False
        for line in lines:
            if CollegeName in line:
                college_exists = True
                break

        with open("CollegeFile.txt","a") as CollegeFile:
            if not college_exists:
                print("This College does not exist.")
                option = input("Do you want to open this college? [y/n] ")
                if option.lower() == "y":
                    CollegeFile.write(f"{CollegeManagement.__CollegeID},")
                    CollegeFile.write(f"{CollegeName},")
                    city = input("Enter City: ")
                    CollegeFile.write(f"{city},")
                    contact_number = input("Enter Contact Number: ")
                    CollegeFile.write(f"{contact_number}")
                    CollegeFile.write("\n")
                    CollegeFile.close()
                    print("College open")
            else:
                print("College already Open.")


    def CollegeDetails(self, CollegeID):
        with open("CollegeFile.txt", "r") as CollegeFile:
            lines = CollegeFile.readlines()

        for line in lines:
            details = line.strip().split(',')
            if len(details) == 4:
                College_Id = details[0]
                College_Name = details[1]
                college_city = details[2]
                college_contact = details[3]
            
            if CollegeID == College_Id:
                print(f"College Name: {College_Name}")
                print(f"City: {college_city}")
                print(f"Contact Number: {college_contact}")
                break
            else:
                print(f"No College found with ID {CollegeID}")


               