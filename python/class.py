class Book:

    def __init__(self, name: str, pages: int):
        self.name = name
        self.pages = pages

    def read(self, pages: int):
        self.pages -= pages
        print(self.pages, 'pages remaining!')


book = Book('Russian Roulette', 200)
book.read(20)
