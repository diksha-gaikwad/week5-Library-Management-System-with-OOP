from .library import Library
from .book import Book
from .member import Member

def menu():
    library = Library()
    library.load_data()

    while True:
        print("\n1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            library.add_book(Book(title, author, isbn))

        elif choice == "2":
            name = input("Name: ")
            member_id = input("Member ID: ")
            library.register_member(Member(name, member_id))

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            print(library.borrow_book(member_id, isbn))

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            print(library.return_book(member_id, isbn))

        elif choice == "5":
            library.save_data()
            break

if __name__ == "__main__":
    menu()