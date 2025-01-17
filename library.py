class LibraryManagementSystem:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print(f"'{title}' already exists in the library.")
        else:
            self.books[title] = {"author": author, "available": True}
            print(f"Book added: '{title}' by {author}")

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title]["available"]:
                self.books[title]["available"] = False
                print(f"You have successfully borrowed '{title}'.")
            else:
                print(f"'{title}' is currently unavailable.")
        else:
            print(f"'{title}' does not exist in the library.")

    def return_book(self, title):
        if title in self.books:
            if not self.books[title]["available"]:
                self.books[title]["available"] = True
                print(f"Thank you for returning '{title}'.")
            else:
                print(f"'{title}' was not borrowed.")
        else:
            print(f"'{title}' does not exist in the library.")

    def view_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            print("\nLibrary Inventory:")
            for title, details in self.books.items():
                status = "Available" if details["available"] else "Borrowed"
                print(f"'{title}' by {details['author']} - {status}")

def main():
    library = LibraryManagementSystem()
    while True:
        print("\nLibrary Management System")
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        elif choice == "3":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == "4":
            library.view_books()
        elif choice == "5":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
