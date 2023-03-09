import uuid
from sqlite3 import connect
from config.settings import Config


class Book:
    def __init__(self, title, genre, author, price, id=None):
        self.id = id if id else str(uuid.uuid1())
        self.title = title
        self.genre = genre
        self.author = author
        self.price = price

    def save(self):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute(
                "INSERT INTO books (id, title, genre, author, price) VALUES (?, ?, ?, ?, ?)",
                (
                    self.id, self.title, self.genre, self.author, self.price
                )
            )
            conn.commit()
        except Exception as ex:
            print('Error saving book: ', ex)
        finally:
            conn.close()

    def delete(self):
        conn = connect(Config.DATABASE_PATH)
        try:
            curr = conn.cursor()
            curr.execute(
                "DELETE FROM books WHERE id=?", (self.id,)
            )
            conn.commit()
        except Exception as ex:
            print('Error deleting book: ', ex)
        finally:
            conn.close()

    def update(self):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute(
                "UPDATE books SET title=?, genre=?, author=?, price=? WHERE id=?",
                (self.title, self.genre, self.author, self.price, self.id)
            )
            conn.commit()
        except Exception as ex:
            print('Error updating book: ', ex)
        finally:
            conn.close()

    @staticmethod
    def create_table():
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    genre TEXT,
                    author TEXT,
                    price REAL
                )
            """)
            conn.commit()
            print('Successfully Created')
        except Exception as ex:
            print('Error creating table: ', ex)
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute(
                "SELECT id, title, genre, author, price FROM books"
            )
            books = curs.fetchall()
            return [{'id': book[0], 'title': book[1], 'genre': book[2], 'author': book[3], 'price': book[4]} for book
                    in books]
        except Exception as ex:
            print('Error getting books: ', ex)
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute(
                "SELECT id, title, genre, author, price FROM books WHERE id=?", (id,)
            )
            book = curs.fetchone()
            if book:
                return {'id': book[0], 'title': book[1], 'genre': book[2], 'author': book[3], 'price': book[4]}
            return None
        except Exception as ex:
            print('Error getting book: ', ex)


if __name__ == '__main__':
    Book.create_table()