from utils import database_sqlite

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choices: """

def menu(USER_CHOICE):
    database_sqlite.create_book_table()
    user_input=input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input=input(USER_CHOICE)        

def prompt_add_book():
    book_name=input("Enter the Book name to be added: ")
    author_name=input("Enter the Author name: ")
    database_sqlite.insert_book(book_name, author_name)
    print(f"Book {book_name} from the author {author_name} added")

def list_books():
    books=database_sqlite.get_all_books()
    for book in books:
        #We can avoid  "if book[read] == 1" as Python internally cosiders 1 as TRUE & 0 as FALSE
        read = 'YES' if book['read'] else 'NO'
        print(f"Book: {book['name']} by Author: {book['author']} - Read: {read}")

def prompt_read_book():
    book_name=input("Enter the name of the book you want to mark as read: ")
    database_sqlite.mark_book_as_read(book_name)

def prompt_delete_book():
    book_name=input("Enter the name of the book you want to delete: ")
    database_sqlite.delete_book(book_name)

menu(USER_CHOICE)