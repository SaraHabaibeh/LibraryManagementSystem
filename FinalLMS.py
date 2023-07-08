import time
import csv
class Book:
    def __init__(self, title, publisher, edition, month, year, language, paperback, isbn10, isbn13, numcopies=1):
        """ """
        self.title = title
        self.publisher = publisher
        self.edition = edition
        self.year = year
        self.month = month
        self.language = language
        self.paperback = paperback
        self.isbn10 = isbn10
        self.isbn13 = isbn13
        self.numcopies = numcopies

    def displaybookinfo(self): 
        """ """
        print(f"Title: {self.title}")
        time.sleep(1)
        print(f"Publisher: {self.publisher}")
        time.sleep(1)
        print(f"Edition: {self.edition}")
        time.sleep(1)
        print(f"Month: {self.month}")
        time.sleep(1)
        print(f"Year: {self.year}")
        time.sleep(1)
        print(f"Language: {self.language}")
        time.sleep(1)
        print(f"Paperback: {self.paperback}")
        time.sleep(1)
        print(f"ISBN-10:{self.isbn10}")
        time.sleep(1)
        print(f"ISBN-13:{self.isbn13}")
        time.sleep(1)
        print(f"Copies available: {self.numcopies}")
        time.sleep(1)
        print()

    def editbook(self, newtitle, newpublisher, newedition, newmonth, newyear, newlanguage, newpaperback, newisbn10, newisbn13):
        """ """
        self.title = newtitle
        self.publisher = newpublisher
        self.edition = newedition
        self.month = newmonth
        self.year = newyear
        self.language = newlanguage
        self.paperback = newpaperback
        self.isbn10 = newisbn10
        self.isbn13 = newisbn13

class Library:
    def __init__(self):
        self.books = []
    def addbook(self, book, replace=False):
        """ """
        for exisbook in self.books:
            if (
                exisbook.title == book.title
                and exisbook.language == book.language
                and exisbook.paperback == book.paperback
                and exisbook.publisher == book.publisher
                and exisbook.month == book.month
                and exisbook.year == book.year
                and exisbook.edition == book.edition
                and exisbook.isbn10 == book.isbn10
                and exisbook.isbn13 == book.isbn13
            ):
                if replace:
                    self.books.remove(exisbook)
                    self.books.append(book)
                    print("Existing book replaced successfully!")
                else:
                    exisbook.numcopies += 1
                    print("Additional copy of the book added successfully!")
                return

        self.books.append(book)
        print("Book added successfully!")

    def removebook(self, searchterm, numcopies=1):
        """ """
        removedcopies = 0
        for book in self.books:
            if (
                searchterm.lower() in book.title.lower()
                or searchterm.lower() in book.publisher.lower()
                or searchterm.lower() == str(book.paperback)
                or searchterm.lower() in book.month.lower()
                or searchterm.lower() == str(book.year)
                or searchterm.lower() in book.language.lower()
                or searchterm.lower() == str(book.edition)
                or searchterm.lower() == str(book.isbn10)
                or searchterm.lower() == str(book.isbn13)
            
            ):
                if book.numcopies > 1:
                    book.numcopies -= 1
                    removedcopies += 1
                    if removedcopies == numcopies:
                        break
                else:
                    self.books.remove(book)
                    removedcopies += 1
                    if removedcopies == numcopies:
                        break

        if removedcopies == 0:
            print("Book not in library")
        elif removedcopies < numcopies:
            print(f"only {removedcopies} copies of the book removed.")
        else:
            print(f"{removedcopies} copies of the book removed.")

    def displaybooks(self,book):
        """ """
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                book.displaybookinfo()

    def archivebooks(self, filename):
        """ """
        try:
            with open(filename, "w") as file:
                for book in self.books:
                    file.write(
                        f"{book.title},{book.publisher},{book.paperback},{book.year},{book.month},{book.language},{book.edition},{book.isbn10},{book.isbn13},{book.numcopies}\n"
                    )
            print("Books archived successfully!")
        except Exception as error:
            print(f"Error archiving books: {error}")

    def genreport(self):
        """ """
        totalbooks = len(self.books)
        uniquebooks = len(set(self.books))
        archivedbooks = 0
        newerthanyear = 0
        publisherdistribution = {}
        yeardistribution = {}

        for book in self.books:
            if book.year not in yeardistribution:
                yeardistribution[book.year] = 1
            else:
                yeardistribution[book.year] += 1

            if book.publisher not in publisherdistribution:
                publisherdistribution[book.publisher] = 1
            else:
                publisherdistribution[book.publisher] += 1

            if book.year > 2020:
                newerthanyear += 1

        archivedbooks = totalbooks - len(self.books)

        print(" Report:")
        print(f"Total books in LMS: {totalbooks}")
        print(f"Unique books offered in LMS: {uniquebooks}")
        print(f"Archived books in LMS: {archivedbooks}")
        print(f"Books newer than 2020: {newerthanyear}")
        print("Book distribution by publisher:")
        for publisher, count in publisherdistribution.items():
            print(f"{publisher}: {count} books")
        print("Book distribution by year:")
        for year, count in yeardistribution.items():
            print(f"{year}: {count} books")


class LMS:
    def __init__(self):
        self.library = Library()

    def menu(self):
        print("Welcome to the Library Management System!")
        self.loadbooks("LMSdata.csv")

        while True:
            print("1. Add a book to LMS")
            print("2. Remove a book from LMS")
            print("3. Search for book in LMS")
            print("4. Edit book information")
            print("5. Generate a report")
            print("6. Archive books")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.addbookmenu()
            elif choice == "2":
                self.removebookmenu()
            elif choice == "3":
                self.library.displaybooks()
            elif choice == "4":
                self.editbookmenu()
            elif choice == "5":
                self.library.genreport()
            elif choice == "6":
                self.archivebooksmenu()
            elif choice == "7":
                self.savebooks("LMSdata.csv")
                print("Thank you for using the Library Management System")
                break
            else:
                print("Invalid choice. Please try again.")

    def addbookmenu(self):
        """ """
        filename = input("Enter the file name: ")
        try:
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    title, publisher, edition, month, year,language, paperback, isbn10, isbn13, numcopies = data
                    numcopies = int(numcopies)
                    book = Book(title, publisher, int(edition), month, int(year), language, int(paperback), int(isbn10), int(isbn13), publisher, numcopies)
                    replace = input("Replace existing book with the same details? (yes/no): ").lower() == "yes"
                    self.library.addbook(book, replace)
        except FileNotFoundError:
            print("File not found.")
        except Exception as error:
            print(f"Error reading the file: {error}")

    def removebookmenu(self):
        """ """
        searchterm = input("Enter any information of the book you want to remove: ")
        numcopies = int(input("Enter the number of copies to remove: "))

        confirmation = input("are you sure you want to remove the book? (y/n): ")
        if confirmation.lower() == "y":
            self.library.removebook(searchterm, numcopies)
            print("Book removed from Library")
        else:
            print("Book could not be removed")


    def editbookmenu(self):
        """ """
        searchterm = input("Enter the title or ISBN number of the book to edit: ")
        availablebooks = self.library.displaybooks(searchterm)
        if not availablebooks:
            print("Book not found.")
            return

        print("Found book(s):")
        for index, book in enumerate(availablebooks):
            print(f"{index + 1}.")
            book.displaybookinfo()

        bookindex = int(input("Enter index of the book you wish to edit: ")) - 1
        if bookindex < 0 or bookindex >= len(availablebooks):
            print("Invalid book index.")
            return
    
        book = availablebooks[bookindex]
        print(f"\nEditing book '{book.title}':")
        book.title = input(f"Enter new title {book.title}")
        book.publisher = input(f"Enter new publisher{book.publisher} ")
        book.edition = int(input(f"Enter new edition {book.edition}"))
        book.month = input(f"Enter new month {book.month}")
        book.year = int(input(f"Enter new year {book.year} "))
        book.language = int(input(f"Enter new Language {book.language}"))\
        
        print("\nBook information updated successfully!")
        confirmation = input("Save changes? (y/n): ")
        if confirmation.lower() == "y":
            self.savebooks("LMSdata.csv")
            print("Books saved successfully!")
        else:
            print("Changes not saved.")
    
    
    def archivebooksmenu(self):
        """ """
        print("\nArchive books:")
        isbn = int(input("Enter the 10 digit ISBN of the book to archive: "))
        numcopies = int(input("Enter the number of copies to archive: "))

        removedcopies = self.library.removebook(isbn, numcopies)
        if removedcopies == None:
            removedcopies = 0
            
        if removedcopies > 0:
            archivedbooks = []
            for book in self.library.books:
                if book.isbn10 == isbn:
                    archivedbooks.append([book.title, book.author, book.pages, book.year, book.publisher, book.numcopies])
            if archivedbooks:
                filename = "LMS.csv"
                try:
                    with open(filename, "a", newline="") as newfile:
                        writer = csv.writer(newfile)
                        writer.writerows(archivedbooks)
                except Exception as error:
                    print(f"Error archiving books: {error}")
            else:
                print("No copies found in the library.")
        else:
            print("No copies found in the library.")

    def loadbooks(self, filename):
        """ """
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    title, publisher, edition, month, year, language, paperback, isbn10, isbn13, numcopies = row
                    book = Book(title, publisher, int(edition), month, int(year), language, int(paperback),int(isbn10), int(isbn13), int(numcopies))
                    self.library.addbook(book)
        except FileNotFoundError:
            print("Starting with an empty library.")
        except Exception as error:
            print(f"Error loading books from file: {error}")

    def savebooks(self, filename):
        """ """
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                for book in self.library.books:
                    writer.writerow([book.title, book.publisher, book.edition, book.month, book.year, book.language, book.paperback, book.isbn10, book.isbn13, book.numcopies])
            print("Books saved successfully!")
        except Exception as error:
            print(f"Error saving books to file: {error}")

lms = LMS()
lms.menu()
               


