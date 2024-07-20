from abc import ABC, abstractmethod

GirlsRooms  = [101, 102, 103, 104, 105]
BoysRooms = [201, 202, 203, 204, 205]


class Hostel(ABC):
  def __init__(self, student_id, BlockNumber):
    self.student_id = student_id
    self.BlockNumber = BlockNumber
    self.RoomNumber = None
    self.Checked = False

  def HostelDetails(self):
    print("Student ID: ", self.student_id)
    print("Block Number: ", self.BlockNumber)
    # print("Room Number: ", self.RoomNumber)

  @abstractmethod
  def CheckIn(self):
    self.Checked = True
    print("Checked In")

  @abstractmethod
  def CheckOut(self):
    self.Checked = False
    print("Checked Out")

class GirlsHostel(Hostel):
  def __init__(self, student_id, BlockNumber):
    super().__init__(student_id, BlockNumber)

  def CheckIn(self):
    if self.Checked == True:
      print("Already Checked In")
    else:
      if len(GirlsRooms) == 0:
        print("No Girls Rooms Available")
        return False
      else:
        self.RoomNumber = GirlsRooms.pop()
        self.Checked = True
        print("Checked In")

  def CheckOut(self):
    if self.Checked == False:
      print("Already Checked Out")
    else:
      GirlsRooms.append(self.RoomNumber)
      self.Checked = False
      self.RoomNumber = None
      print("Checked Out")

class BoysHostel(Hostel):
  def __init__(self, student_id, BlockNumber):
    super().__init__(student_id, BlockNumber)

  def CheckIn(self):
    if self.Checked == True:
      print("Already Checked In")
    else:
      if len(BoysRooms) == 0:
        print("No Girls Rooms Available")
        return False
      else:
        self.RoomNumber = BoysRooms.pop()
        self.Checked = True
        print("Checked In")

  def CheckOut(self):
    if self.Checked == False:
      print("Already Checked Out")
    else:
      BoysRooms.append(self.RoomNumber)
      self.Checked = False
      self.RoomNumber = None
      print("Checked Out")
