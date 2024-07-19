class Canteen:
    def __init__(self, InchargeId, ItemsList, AvailableList):
        self.InchargedId = InchargeId
        self.ItemsList = ItemsList
        self.AvailableList = AvailableList

    def ShowItems(self):
        print("Items which are present in the canteen: ", self.ItemsList)

    def Buy(self,Item):
        if Item in self.AvailableList:
            print(f"Bought {Item}.")
        else:
            print(f"{Item} is not available.")


class Library:
    def __init__(self, LibraryId, LibrarianName, BookSection, TotalBooks):
        self.LibraryId = LibraryId
        self.LibrarianName = LibrarianName
        self.BookSection = BookSection
        