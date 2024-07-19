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