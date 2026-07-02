import json
from models.book import Book
from models.member import Member

class Library:
    """Manages books and members in the library."""
    total_books = 0
    total_members = 0

    def __init__(self):
        self.books = {}
        self.members = {}

    @classmethod
    def stats(cls):
        return (
            f"Total books: {cls.total_books}\n"
            f"Total members: {cls.total_members}"
        )

    @classmethod
    def create_empty(cls):
        return cls()

    def add_book(self, book):
        """Adds a new book to the library."""
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            Library.total_books += book.copies
        else:
            print("The book already exists")

    def add_member(self, member):
        self.members[member.member_id] = member
        Library.total_members += 1

    def show_books(self):
        if not self.books:
            print("No books")

        for b in self.books.values():
            print(b)

    def search(self, word):
        found = []

        for b in self.books.values():
            if (
                word.lower() in b.title.lower()
                or
                word.lower() in b.author.lower()
            ):
                found.append(b)

        return found

    def borrow(self, member_id, isbn):
        """Allows a member to borrow a book."""

        if member_id not in self.members:
            print("Member not found")
            return

        if isbn not in self.books:
            print("Book not found")
            return

        if self.books[isbn].borrow():
            self.members[member_id].borrow_book(isbn)
            print("Borrowed successfully")
        else:
            print("Book unavailable")

    def return_book(self, member_id, isbn):
        if (
            member_id in self.members
            and isbn in self.members[member_id].borrowed
        ):
            self.books[isbn].return_book()
            self.members[member_id].return_book(isbn)
            print("Returned")

    def save(self):
        """Saves library books to a JSON file."""

        data = []

        for b in self.books.values():
            data.append({
                "title": b.title,
                "author": b.author,
                "isbn": b.isbn,
                "copies": b.copies
            })

        with open("library.json", "w") as f:
            json.dump(data, f)

    def load(self):
        """Loads books from a JSON file."""

        try:
            with open("library.json", "r") as f:
                data = json.load(f)

            for i in data:
                self.add_book(
                    Book(
                        i["title"],
                        i["author"],
                        i["isbn"],
                        i["copies"]
                    )
                )

        except:
            print("File not found")
