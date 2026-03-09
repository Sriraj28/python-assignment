class Library:
    def __init__(self):
        self.books = {"Python": True, "Java": True}

    def display(self):
        for book, status in self.books.items():
            print(book, "-", "Available" if status else "Checked Out")

    def checkout(self, name):
        if self.books.get(name):
            self.books[name] = False
        else:
            print("Not Available")

    def return_book(self, name):
        self.books[name] = True


lib = Library()
lib.display()
lib.checkout("Python")
lib.display()