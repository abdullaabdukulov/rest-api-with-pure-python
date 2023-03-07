import uuid
from sqlite3 import connect
from Bookmarks.config.settings import Config


class Author:
    def __init__(self, name, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.name = name

    def save(self):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            if self.id:
                curs.execute(
                    "UPDATE authors SET name=? WHERE id=?",
                    (
                        self.name, self.id
                    )
                )
            else:
                curs.execute(
                    "INSERT INTO authors (id, name) VALUES (?, ?)",
                    (
                        self.id, self.name
                    )
                )
            conn.commit()
        except Exception as ex:
            print('Error saving author: ', ex)

        finally:
            conn.close()

    def delete(self):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute(
                "DELETE FROM authors WHERE id=?", (self.id, )
            )
            conn.commit()
        except Exception as ex:
            print('Error deleting author: ', ex)

