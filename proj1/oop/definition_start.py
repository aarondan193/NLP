class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def setdiscount(self, amount):
        self._discount = amount
    
b1 = Book("Brave New World", "Leo Tolestoy", 1225, 39.95)
b2 = Book("War and Peace", "JD Salinger", 234, 29.95)


print(b1.getprice())

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())