library = {
"978-0132350884": {"title": "Clean Code", "author": "Robert C. Martin"},
"978-0201485677": {"title": "Refactoring", "author": "Martin Fowler"},
}

users = {
"Alice": [],
"Bob": [],
}


class Library:

    def __init__(self, library, users) -> None:
        self.library = library
        self.users = users

    def add_new_book(self,ISBN,title,author):
        book = {
            "title": title,
            "author": author
        }
        self.library[ISBN] = book
        return "New book added"
    
    def remove_book(self,ISBN):
        name = self.library[ISBN]["title"]
        del self.library[ISBN]
        return f"\"{name}\" has been removed from the library!"
    
    def register_user(self,name):
        self.users[name] = []
        return f"New user registered"
    
    def borrow_book(self,name,ISBN):
        self.users[name].append(ISBN)
        return f"{name} borrowed book \"{ISBN}\""
    
    def return_book(self,name,ISBN):
        self.users[name].remove(ISBN)
        return f"{name} retured book {ISBN}"
    
    def borrowed_books(self,name):
        return self.users[name]


        

uyoLib = Library(library,users)


print(uyoLib.add_new_book("445-6677787","Rich Dad poor dad","Robert Kiyosaki"))
print(uyoLib.add_new_book("997-8889871","Here we go","Kim jung uh"))
print(uyoLib.add_new_book("987-8553987","The new world","Kim jung uh"))
print(uyoLib.register_user("Godswill"))
print(uyoLib.borrow_book("Godswill","997-8889871"))
print(uyoLib.borrow_book("Alice","978-0201485677"))
print(uyoLib.return_book("Godswill","997-8889871"))
print(uyoLib.borrowed_books("Alice"))
print(uyoLib.remove_book("987-8553987"))

