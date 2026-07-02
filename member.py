class Member:
    """Represents a library member."""

    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed = []
        self.history = []

    @property
    def member_id(self):
        return self.__member_id

    @property
    def borrowed(self):
        return self.__borrowed

    def borrow_book(self, isbn):
        self.__borrowed.append(isbn)
        self.history.append(f"Borrowed {isbn}")

    def return_book(self, isbn):
        if isbn in self.__borrowed:
            self.__borrowed.remove(isbn)
            self.history.append(f"Returned {isbn}")

    def __str__(self):
        return f"{self.__name} ({self.member_id})"

    def __repr__(self):
        return self.__str__()
