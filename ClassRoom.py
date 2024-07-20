
class Classroom:
    def __init__(self, ClassId = None , Section = None, DepartmentId = None):
        self.ClassId = ClassId
        self.Section = Section
        self.DepartmentId = DepartmentId

    def ClassroomDetails(self):
        print("Class ID: ", self.ClassId)
        print("Section: ", self.Section)
        print("Department ID: ", self.DepartmentId)


    def AddClassRoom(self,ClassId, Section, DepartmentId):
        try:
            with open("ClassRoom.txt", "a") as class_File:
                class_File.write(f"{ClassId},")
                class_File.write(f"{Section},")
                class_File.write(f"{DepartmentId}\n")
                print("Class Room added successfully.")
        except FileNotFoundError:
            print("Error: ClassRoom.txt not found.")


    def ClassroomDetails(self,ClassID):
        try:
            with open ("ClassRoom.txt","r") as class_File:
                lines = class_File.readlines()
        except FileNotFoundError:
            lines = []

        for line in lines:
            class_details = line.strip().split(',')
            if len(class_details) == 3:
                id_class = class_details[0]
                section_id = class_details[1]
                department_id = class_details[2]
            if id_class == ClassID:
                print(f"Section : {section_id}")
                print(f"Department ID: {department_id}")
                print("\n")
              

    def IsOccupied(self,class_ID):
        num_of_deprtment = 0
        try:
            with open ("ClassRoom.txt","r") as class_File:
                lines = class_File.readlines()
        except FileNotFoundError:
            lines = []

        for line in lines:
            class_details = line.strip().split(',')
            if len(class_details) == 3:
                id_class = class_details[0]
                section_id = class_details[1]
                department_id = class_details[2]
            if id_class == class_ID:
                num_of_deprtment += 1
            
        if num_of_deprtment > 6:
            print("Classroom is occupied")
        else:
            print("Classroom is NOT occupied")
        