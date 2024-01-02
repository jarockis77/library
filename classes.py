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
            self.bookslist.append(book)
            print("Book added")

    def returnbook(self, book):
        if book in self.lenderDict.keys():
            self.lenderDict.pop(book)
            print("Book Returned Succesfully")
        else:
            print("The book does not exist in the book lending database")

        def main():
            while (True):
                print(f"Welcome to the {Library.name} library.Following are the options,")
                choice = """
                1.Display Books
                2.Lend a Book
                3.Add a Book
                4.Return a Book
                """
                print(choice)

                userinput = input("Press Q to quit and C to continue:")
                if userinput == 'C':
                    userchoice = int(input("select an option to continue:"))
                    if userinput == 1:
                        Library.displayBooks()
                    elif userinput == 2:
                        book = input("Enter the name of the book you want to lend:")
                        user = input("Enter the name of the user:")
                        Library.lendBook(book, user)

                    elif userchoice == 3:
                        book = input("enter the name of the book you want to add:")

                        Library.addBook(book)
                    elif userchoice == 4:
                        book = input("Enter the name of the book you would like to return:")
                        Library.returnbook(book)
                    else:
                        print("Please choose a valid option")

                elif userinput == "Q":
                    break

                else:
                    print("Please enter a valid option")
