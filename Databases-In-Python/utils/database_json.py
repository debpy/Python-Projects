import json

"""
Concerned with storing & retrieving books from a json file
Format of the json file:
[

    {
        'name': 'Clean Code',
        'author': 'Robert',
        'read': True
    }

]
"""
books_file='books.json'

def create_book_table():
    with open(books_file, 'w') as f:
        json.dump([],f)        

def get_all_books():
    with open(books_file, 'r') as f:
        return json.load(f)
        
def insert_book(name, author):
    with open(books_file, 'a') as f:
        books=get_all_books()
        books.append({'name': name, 'author': author, 'read': False})
        _save_all_books(books)

        
def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read']=True
        _save_all_books(books)

def _save_all_books(books):
    with open(books_file, 'w') as f:
        json.dump(books, f)

def delete_book(name):
    books=get_all_books()
    books=[ book  for book in books if book['name'] != name ]
    _save_all_books(books)