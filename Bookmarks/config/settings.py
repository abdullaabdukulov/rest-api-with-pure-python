import os


class Config:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'books.db')