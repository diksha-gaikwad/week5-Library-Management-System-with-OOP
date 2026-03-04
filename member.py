class Member:
    MAX_BORROW = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            return False, "Borrow limit reached"

        self.borrowed_books.append(isbn)
        return True, "Book added"

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True, "Book removed"
        return False, "Book not found"