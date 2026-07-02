class Book:
    """Represents a book in the library."""

    @staticmethod
    def valid_copies(copies):
        return copies > 0

    def __init__(self, title, author, isbn, copies=1):
        if not Book.valid_copies(copies):
            raise ValueError("Invalid copies")

        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__copies = copies
        self.__available = copies

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__available

    @property
    def copies(self):
        return self.__copies

    def borrow(self):
        """Borrows one available copy of the book."""
        if self.__available > 0:
            self.__available -= 1
            return True
        return False

    def return_book(self):
        """Returns one borrowed copy."""
        if self.__available < self.__copies:
            self.__available += 1

    def __str__(self):
        return (
            f"{self.title} | {self.author} | "
            f"{self.available}/{self.copies}"
        )

    def __repr__(self):
        return self.__str__()


class FictionBook(Book):
    pass


class NonFictionBook(Book):
    pass
