class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
b=Book('Pytho', 'Jose', 45)
print(b)#  wrong. if no __str__ -> string rep of class
print(str(b))
print(len(b))
del b#book del
print(str(b))
