import uuid
from sqlite3 import connect
from config.settings import Config


class Author:
    def __init__(self, name, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.name = name

    def save(self):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
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

    @staticmethod
    def create_table():
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute("""
                CREATE TABLE IF NOT EXISTS authors (
                    id TEXT PRIMARY KEY,
                    name TEXT
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
                "SELECT id, name FROM authors"
            )
            authors = curs.fetchall()
            return [{'id': author[0], 'name': author[1]} for author in authors]
        except Exception as ex:
            print('Error getting authors: ', ex)
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        conn = connect(Config.DATABASE_PATH)
        try:
            curs = conn.cursor()
            curs.execute(
                "SELECT id, name FROM authors WHERE id=?", (id, )
            )
            author = curs.fetchone()
            if author:
                return {'id': author[0], 'name': author[1]}
            return None
        except Exception as ex:
            print('Error getting author: ', ex)
        finally:
            conn.close()


if __name__ == '__main__':
    Author.create_table()