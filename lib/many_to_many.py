class Author:

    contracts_list = []
    author_list = []
    def __init__(self,name):
        self.name = name 
        Author.author_list.append(self)
    def contracts(self):
        author_contracts = [contract for contract in Contract.all if contract.author == self]
        return author_contracts
    def books(self):
        author_books = [book for book in Book.books_list]
        return author_books
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:

    books_list = []
    def __init__(self, title):
        self.title = title
        Book.books_list.append(self)
    
    def contracts(self):
        book_contracts = [contract for contract in Contract.all if contract.book == self]
        return book_contracts
    
    def authors(self):
        author_list = [contract.author for contract in Contract.all if contract.book == self]
        return author_list

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)
        Author.contracts_list.append(self)
        Contract.all.append(self)

    def set_author(self, author):
        if isinstance(author, Author):
            self.author = author
        else:
            raise ValueError("Author must be an instance of the Author class.")

    def set_book(self, book):
        if isinstance(book, Book):
            self.book = book
        else:
            raise ValueError("Book must be an instance of the Book class.")

    def set_date(self, date):
        if isinstance(date, str):
            self.date = date
        else:
            raise ValueError("Date must be a string.")

    def set_royalties(self, royalties):
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise ValueError("Royalties must be an integer.")

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
