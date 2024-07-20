incharge_id = 1
items_list = ["Sandwich", "Burger", "Pizza", "Soda", "Juice"]
available_list = ["Burger", "Pizza", "Soda"]


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


class Library:
    def __init__(self, LibraryId, LibrarianName, BookSection, TotalBooks):
        self.LibraryId = LibraryId
        self.LibrarianName = LibrarianName
        self.BookSection = BookSection
        self.TotalBooks = TotalBooks
        