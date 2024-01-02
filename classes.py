class Library:

    def __init__(self, bookslist, name):
        self.bookslist = bookslist
        self.name = name
        self.lenderDict = {}

    def displayBooks(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, book, user):

            if book not in self.lenderDict.keys():
                self.lenderDict.update({book: user})
                print("Book has been lended, Database updated.")
            else:
                print(f"Book is already being used by {self.lenderDict[book]}")
        # else:
        #     print("Apologies! We don't have this book in our library")

    def addBook(self, book):
        if book in self.bookslist:
            print("Book already exists")
        else:
            self.booksList.append(book)
            print("Book added")



    def returnbook(self, book):
        if book in self.lenderDict.keys():
            self.lenderDict.pop(book)
            print("Book Returned Succesfully")
        else:
            print("The book does not exist in the book lending database")


