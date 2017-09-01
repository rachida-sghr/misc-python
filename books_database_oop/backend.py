import sqlite3


class Database:

    def __init__(self, database):
        self.connection = sqlite3.connect("books.db")
        self.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRiMARY KEY , title TEXT, author TEXT, year INTEGER, country TEXT, borrowed TEXT)")

    def insert(self, title, author, year, country, borrowed):
        cmd = "INSERT INTO books VALUES(NULL,?,?,?,?,?)"
        self.execute(cmd, title, author, year, country, borrowed)

    def view(self):
        return self.fetch("SELECT * FROM books")

    def search(self, title="", author="", year="", country="", borrowed=""):
        cmd = "SELECT * FROM books WHERE title=? OR author=? OR year=? OR country=? OR borrowed=?"
        return self.fetch(cmd, title, author, year, country, borrowed)

    def delete(self, id):
        self.execute("DELETE FROM books WHERE id=?", id)

    def update(self, id, title, author, year, country, borrowed):
        cmd = "UPDATE books SET title=?, author=?, year=?, country=?, borrowed=? WHERE id=?"
        self.execute(cmd, title, author, year, country, borrowed, id)

    def execute(self, sql_cmd, *params):
        self.connection.cursor().execute(sql_cmd, params)
        self.connection.commit()

    def fetch(self, sql_cmd, *params):
        cursor = self.connection.cursor().execute(sql_cmd, params)
        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
