"""
Concerned with storing and retrieving books from a list
"""
from pickle import GLOBAL
import json
import sqlite3
from typing import List,Dict,Union

from DatabaseInPython.utils.database_connection import DatabaseConnection

books=[]
# book = Dict(str , Union(str, int))
file_name='books.json'


def create_book_table() -> None:
    # with open(file_name,'w') as file:
    #     json.dump([],file)
    # connection = sqlite3.connect('data.db')
    # cursor = connection.cursor()
    # cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')
    #
    # connection.commit()
    # connection.close()

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')





def add_book(name,author) -> None:
    # books_data = list_books()
    # books_data.append({'name':name,'author':author,'read':False})
    # _save_all_books(books_data)
    # with open(file_name,'a') as file:
    #     file.write(f'{name},{author},0 \n')

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES(?,?,0)",(name,author))

def list_books() :
    # with open(file_name,'r') as file:
    #     return json.load(file)
    #     books_datas = [line.strip().split(',') for line in file.readlines()]
    # return [
    #     {'name': list_data[0],'author':list_data[1], 'read':list_data[2]}
    #     for list_data in books_datas
    # ]
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books_data = [{'name':row[0],'author': row[1] , 'read':row[2]} for row in cursor.fetchall()]

    return books_data

# def _save_all_books(books_data):
#     with open(file_name,'w') as file:
#         # for book in books_data:
#         #     file.write(f'{book["name"]},{book["author"]},{book["read"]}\n')
#         json.dump(books_data,file)

def mark_book_as_read(name)  :
    # books_data = list_books()
    # for book in books_data:
    #     if book['name'] == name:
    #         book['read'] = True
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))
    # _save_all_books(books_data)



def delete_book(name):
    # global books
    # books = list_books()
    # books = [book for book in books if book['name'] != name]
    # _save_all_books(books)
    ## With DATABASE
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE name=?", (name,))



# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)


