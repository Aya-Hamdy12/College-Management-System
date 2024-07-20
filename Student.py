import College
from abc import ABC, abstractmethod

class Student(ABC):
    __num_of_student = 0
    def __init__(self, StudentName = None, Gender = None, Year = None, ClassId = None):
        Student.__num_of_student += 1
        self.__StudentId = Student.__num_of_student
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
    def set_ClassId(self,ClassId):
        self.__ClassId = ClassId


    def AddStudent(self,ID_College, ID_Student, ID_class,Student_name, gender, Year, payfees):
        try:
            with open ("StudentDetails.txt","r") as StudentFiles:
                lines = StudentFiles.readlines()

        except FileNotFoundError:
            lines = []

        student_status = False

        for line in lines:
            studen_details = line.strip().split(',')
            if len(studen_details) == 7:
                id_College = studen_details[0]
                id_Student = studen_details[1]
                id_class = studen_details[2]
                # gen = studen_details[3]
                # date = studen_details[4]
                # payfees = studen_details[5]
            if ID_College == id_College and ID_Student == id_Student and ID_class == id_class:
                student_status = True
                break

        if not student_status:
            with open("StudentDetails.txt","a") as StudentFiles:
                StudentFiles.write(f"{ID_College},")
                StudentFiles.write(f"{Student.__num_of_student},")
                StudentFiles.write(f"{ID_class},")
                StudentFiles.write(f"{Student_name},")
                StudentFiles.write(f"{gender},")
                StudentFiles.write(f"{Year},")
                StudentFiles.write(f"{payfees}\n")
                StudentFiles.close()
                print("The student has successfully enrolled in the university.")
        else:
            print("This student already exists")

    @abstractmethod
    def StudentDetails(self):
        pass


    def PayFees(self):
        # print("This method contains the payment status of each student.")
        try:
            with open ("StudentDetails.txt","r") as payFees_File:
                lines = payFees_File.readlines()
        except FileNotFoundError:
            lines = []

        for line in lines:
            studen_details = line.strip().split(',')
            if len(studen_details) == 7:
                id_Student = studen_details[2]
                student_name = studen_details[3]
                payfees = studen_details[6]
            if payfees == "y":
                print(f"Student Name: {student_name}")
                print(f"Student ID: {id_Student}")
                print(f"Payment status: Paid")
                print("\n")
            else:
                print(f"Student Name: {student_name}")
                print(f"Student ID: {id_Student}")
                print(f"Payment status: NOT Paid")
                print("\n")




    def IsPresent(self,StudentId,Date):
        with open("StudentDetails.txt","r") as StudentFiles:
            lines = StudentFiles.readlines()

        Student_is_present = False

        for line in lines:
            studen_details = line.strip().split(',')
            if len(studen_details) == 7:
                id_Student = studen_details[2]
                date = studen_details[5]
            if StudentId == id_Student and Date == date:
                Student_is_present = True
                break
     
        if not Student_is_present:
            print("The student Does Not Exist")
        elif Student_is_present and (int(date) < 2018):
            print("The student has already graduated")
        else:
            print("The student is present")






class UGStudent(Student):
    def __init__(self, StudentName=None, Gender=None, Year=None, ClassId=None):
        super().__init__(StudentName, Gender, Year, ClassId)

    def StudentDetails(self, Student_ID):
        try:
            with open ("StudentDetails.txt","r") as StudentFiles:
                lines = StudentFiles.readlines()

        except FileNotFoundError:
            lines = []
        Student = False
        for line in lines:
            studen_details = line.strip().split(',')
            if len(studen_details) == 7:
                id_College = studen_details[0]
                id_Student = studen_details[1]
                id_class = studen_details[2]
                student_name = studen_details[3]
                gen = studen_details[4]
                date = studen_details[5]
                # payfees = studen_details[6]

            if Student_ID == id_Student:
                Student = True
                break
            
        if not Student:
            print("This Student does not exist in college.")
        else:
            print("The Student Information")
            print(f"Student Name: {student_name}")
            print(f"College ID: {id_College}")
            print(f"Class ID: {id_class}")
            print(f"Gender : {gen}")
            print(f"Year of joining college: {date}")





class PGStudent(Student):
    def __init__(self, StudentName=None, Gender=None, Year=None, ClassId=None):
        super().__init__(StudentName, Gender, Year, ClassId)


    def StudentDetails(self, Student_ID):
        try:
            with open ("StudentDetails.txt","r") as StudentFiles:
                lines = StudentFiles.readlines()

        except FileNotFoundError:
            lines = []
        Student = False
        for line in lines:
            studen_details = line.strip().split(',')
            if len(studen_details) == 7:
                id_College = studen_details[0]
                id_Student = studen_details[1]
                id_class = studen_details[2]
                student_name = studen_details[3]
                gen = studen_details[4]
                date = studen_details[5]
                # payfees = studen_details[6]
            if Student_ID == id_Student:
                Student = True
                break
                    
        if not Student:
            print("This Student does not exist in college.")
        else:
            print("The Student Information")
            print(f"Student Name: {student_name}")
            print(f"Graduated from College ID: {id_College}")
            print(f"Graduated from the department ID: {id_class}")
            print(f"Gender : {gen}")
            print(f"Graduation Year: {date}")
