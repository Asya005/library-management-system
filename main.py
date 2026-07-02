from models.book import Book
from models.member import Member
from services.library import Library

def menu():
    """Runs the library menu."""
    lib = Library.create_empty()
    while True:
        print("\n1 Add book")
        print("2 Show")
        print("3 Add member")
        print("4 Borrow")
        print("5 Return")
        print("6 Search")
        print("7 Stats")
        print("8 Save")
        print("9 Load")
        print("0 Exit")
        try:
            c = input("Choose ")

            if c == "1":
                b = Book(
                    input("Title: "),
                    input("Author: "),
                    input("ISBN: "),
                    int(input("Copies: "))
                )
                lib.add_book(b)

            elif c == "2":
                lib.show_books()

            elif c == "3":
                lib.add_member(
                    Member(
                        input("Name: "),
                        input("ID: ")
                    )
                )

            elif c == "4":
                lib.borrow(
                    input("Member ID: "),
                    input("ISBN: ")
                )

            elif c == "5":
                lib.return_book(
                    input("Member ID: "),
                    input("ISBN: ")
                )

            elif c == "6":
                r = lib.search(input("Search: "))

                for i in r:
                    print(i)

            elif c == "7":
                print(Library.stats())

            elif c == "8":
                lib.save()

            elif c == "9":
                lib.load()

            elif c == "0":
                break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    menu()


