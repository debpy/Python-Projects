"""
Concerned with storing & retrieving books from a csv file
Format of the csv file:

name,author,read
"""
books_file="books.txt"

def create_book_table():
    with open(books_file, 'w'):
        pass

def get_all_books():
    with open(books_file, 'r') as f:
        lines = [line.strip().split(',') for line in f.readlines()]
        books = [ {'name': line[0], 'author': line[1], 'read': line[2]} for line in lines ]
        return books
    
def insert_book(name, author):
    with open(books_file, 'a') as f:
        f.write(f"{name}, {author}, 0 \n")

def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read']=1
        _save_all_books(books)

def _save_all_books(books):
    with open(books_file, 'w') as f:
        for book in books:
            f.write(f"{book['name']},{book['author']},{book['read']}\n")

def delete_book(name):
    books=get_all_books()
    books=[ book  for book in books if book['name'] != name ]
    _save_all_books(books)