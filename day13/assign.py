class book:
    print()
    print("=====Book Recommendations")
    print()

    def __init__(self, Title, Author, Pages):
        self.title = Title
        self.author = Author
        self.no_of_pages = Pages

    def descripton(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.no_of_pages}")

CA = book("When a past came calling", "Chinua Achebe", 119)
CA.descripton()

print()

MH = book("Psychology of money", "Morgan Housel", 105)
MA.descripton()
