import uuid
from sqlite3 import connect
from Bookmarks.config.settings import Config


class Book:
    def __init__(self, title, genre, author, price, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.title = title
        self.genre = genre
        self.author = author
        self.price = price

    def save(self):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            if self.id:
                curs.execute(
                    "UPDATE books SET title=?, genre=?, author=?, price=? WHERE id=?", (
                        self.title, self.genre, self.author, self.price, self.id)
                )
            else:
                curs.execute(
                    "INSERT INTO books (id, title, genre, author, price) VALUES (?, ?, ?, ?)",
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
