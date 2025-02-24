class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum number of books (3).")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            raise BookNotFoundException(f"{self.name} did not borrow '{book.title}'.")

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = self._find_member(member_name)
        book = self._find_book(book_title)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self._find_member(member_name)
        book = self._find_book(book_title)
        member.return_book(book)

    def _find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        raise ValueError(f"Member '{name}' not found.")

    def _find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def __str__(self):
        return f"Library: {len(self.books)} books, {len(self.members)} members"

# Test Scenarios
if __name__ == "__main__":
    library = Library()

    # Adding books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book4 = Book("Moby Dick", "Herman Melville")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Adding members
    member1 = Member("Alice")
    member2 = Member("Bob")

    library.add_member(member1)
    library.add_member(member2)

    # Borrowing books
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "The Great Gatsby")
        print(member1)  # Should show Alice with 3 borrowed books
    except MemberLimitExceededException as e:
        print(e)

    try:
        library.borrow_book("Alice", "Moby Dick")  # Should raise MemberLimitExceededException
    except MemberLimitExceededException as e:
        print(e)

    try:
        library.borrow_book("Bob", "1984")  # Should raise BookAlreadyBorrowedException
    except BookAlreadyBorrowedException as e:
        print(e)

    try:
        library.borrow_book("Bob", "Non-existent Book")  # Should raise BookNotFoundException
    except BookNotFoundException as e:
        print(e)

    # Returning books
    try:
        library.return_book("Alice", "1984")
        print(member1)  # Should show Alice with 2 borrowed books
    except BookNotFoundException as e:
        print(e)

    try:
        library.return_book("Alice", "Non-existent Book")  # Should raise BookNotFoundException
    except BookNotFoundException as e:
        print(e)