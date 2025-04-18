class Item:
    def __init__(self, title):
        self.title = title

    def describe(self):
        print(f"This item is titled '{self.title}'.")

# attributes: title, author, pages, genre, price
class Book(Item):
    def __init__(self, title, author, pages, genre, price):
        super().__init__(title) 
        self.author = author
        self.pages = pages
        self.genre = genre
        self.__price = price  

    def read(self):
        print(f"You are reading '{self.title}' by {self.author}.")

    def get_summary(self):
        return f"'{self.title}' is a {self.genre} book with {self.pages} pages."

    def get_price(self):  
        return f"The price of this book is ${self.__price}."

#  Book object
book1 = Book("she said No", "Margaret Gitau", 300, "Tech Fiction", "50.00")

# Use the Book methods
book1.describe()
book1.read()
print(book1.get_summary())
print(book1.get_price())
