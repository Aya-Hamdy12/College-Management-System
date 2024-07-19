import json
import re
from abc import ABC, abstractmethod


class CollegeManagement:
    def __init__(self,CollegeName):
        self.__CollegeName = CollegeName
        self.__City = ""
        self.__ContactNumber = ""



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
                    print(" College allready Open.\n")
            else:
                print("This College is open.")
               
                    
    def CollegeDetails(self,CollegeName):
        with open("CollegeFile.txt", "r") as CollegeFile:
                    data = CollegeFile.read()
        pattern = r"College Name: (.*)\nCity: (.*)\nContact Number: (\d+)\n"
        matches = re.findall(pattern, data)
        for college_name,city_of,contact_number in matches:
             if college_name == CollegeName:
                 print(f"Department ID: {CollegeName} \n City: {city_of} \n Contact Number:  {contact_number}")
        
        