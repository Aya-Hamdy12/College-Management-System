import CollegeManagement


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