class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lenderDict = {}

    def displayBooks(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)