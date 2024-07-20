incharge_id = 1
items_list = ["Sandwich", "Burger", "Pizza", "Soda", "Juice"]
available_list = ["Burger", "Pizza", "Soda"]

# Define the Canteen class
class Canteen:
    def __init__(self, InchargeId=None, ItemsList=None, AvailableList=available_list):
        self.InchargedId = InchargeId
        self.ItemsList = ItemsList
        self.AvailableList = AvailableList

    def ShowItems(self):
        print(f"Items which are present in the canteen: ", self.AvailableList)

    def Buy(self, Item):
        if Item in available_list:
            print(f"Bought {Item}.")
        else:
            print(f"{Item} is not available.")


# Create an instance of the Canteen class
canteen = Canteen(incharge_id, items_list, available_list)

# Test ShowItems method
canteen.ShowItems()

# Test Buy method with an item that is available
canteen.Buy("Pizza")

# Test Buy method with an item that is not available
canteen.Buy("Juice")

# Test Buy method with an item that is not in the items list at all
canteen.Buy("Hotdog")


class Library:
    def __init__(self, LibraryId, LibrarianName, BookSection, TotalBooks):
        self.LibraryId = LibraryId
        self.LibrarianName = LibrarianName
        self.BookSection = BookSection
        