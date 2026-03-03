# we are using sqllite
from DatabaseInPython.utils.database import create_book_table
from utils.database import add_book,mark_book_as_read,delete_book,list_books


USER_CHOICE  = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""

def menu():
    create_book_table()
    user_input= input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
           print("Unknown command !! please try again")

        user_input= input(USER_CHOICE)



# def prompt_add_book() ask for book name and author
# def list_books() show all the books inside the list
# def prompt_read_book() ask for book name and change it to "read" in our list
# def prompt_delete_book() ask for book name and remove that from book list


def prompt_add_book():
    name = input("Enter book name: ")
    author = input("Enter book author: ")

    add_book(name, author)

def list_all_books():
    books = list_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f'{book["name"]} by {book["author"]} , read : {read}')

def prompt_read_book():
    name = input("Enter book name: ")
    mark_book_as_read(name)

def prompt_delete_book():
    name = input("Enter book name: ")
    delete_book(name)




menu()