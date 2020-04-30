from .database_connection import DatabaseConnection

"""
Concerned with storing & retrieving books from a sqlite database

"""

def create_book_table():
    with DatabaseConnection('data.db') as connection:        
        cursor = connection.cursor()
        cursor.execute('CREATE table IF NOT EXISTS books(name text PRIMARY KEY , author text, read integer)')

def get_all_books():
    with DatabaseConnection('data.db') as connection: 
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books;')
    
    #It fetches all the rows in the table
    ##books = cursor.fetchall() #[(name, author, read),((name, author, read)]
    #Converting it to list of dictionaries for maintaing uniformity in data structure
        books = [ {'name':row[0], 'author':row[1], 'read': row[2]} for row in cursor.fetchall()]
    
    #As we are NOT writing anything to the database, we are reading from it
    #connection.commit()
    return books

def insert_book(name, author):
    # ";0);DROP TABLE books;
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
    #The below approach is NOT recommended
    #cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)';)
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)',(name, author))
    #cursor.execute('INSERT INTO books VALUES(?, ?, 0)',(name, author))

        
def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        #The (name,) needs to be specified as a TUPLE so that it doesnot consider it arithmetic operator
        cursor.execute('UPDATE books SET read =1 WHERE name=?',(name, ))

def delete_book(name):
    with DatabaseConnection('data.db') as connection:
        
        cursor = connection.cursor()
        #The (name,) needs to be specified as a TUPLE so that it doesnot consider it arithmetic operator
        cursor.execute('DELETE FROM books WHERE name = ?',(name,))