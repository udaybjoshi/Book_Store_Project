"""
Concerned with storing and retrieving books from a sqlite db.
"""

from .database_connection import DatabaseConnection


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # SQLite automatically makes `integer primary key` row auto-incrementing
        cursor.execute('CREATE TABLE IF NOT EXISTS books (id integer primary key, name text, author text, '
                       'read integer default 0)')


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books


def insert_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books (name, author) VALUES (?, ?)', (name, author))

def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

        connection.commit()
        connection.close()


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))

        connection.commit()
        connection.close()