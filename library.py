import json
from .book import Book
from .member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member or not book:
            return False, "Invalid member or book"

        status, msg = book.check_out(member_id)
        if status:
            member.borrow_book(isbn)
        return status, msg

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if not member or not book:
            return False, "Invalid member or book"

        book.return_book()
        member.return_book(isbn)
        return True, "Returned successfully"

    def save_data(self):
        with open("data/books.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f)

        with open("data/members.json", "w") as f:
            json.dump({k: v.__dict__ for k, v in self.members.items()}, f)

    def load_data(self):
        try:
            with open("data/books.json", "r") as f:
                books = json.load(f)
                for k, v in books.items():
                    self.books[k] = Book.from_dict(v)
        except:
            pass

        try:
            with open("data/members.json", "r") as f:
                members = json.load(f)
                for k, v in members.items():
                    member = Member(v["name"], v["member_id"])
                    member.borrowed_books = v["borrowed_books"]
                    self.members[k] = member
        except:
            pass