import sqlite3


class Database:

    def __init__(self, database):
        self.connection = sqlite3.connect("books.db")
        self.connection.cursor().execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRiMARY KEY , title TEXT, author TEXT, year INTEGER, country TEXT, borrowed TEXT)")
        self.connection.commit()

    def insert(self, title, author, year, country, borrowed):
        self.connection.cursor().execute("INSERT INTO books VALUES(NULL,?,?,?,?,?)",(title, author, year, country, borrowed))
        self.connection.commit()

    def view(self):
        self.connection.cursor().execute("SELECT * FROM books")
        rows=self.connection.cursor().fetchall()
        return rows

    def search(self, title="", author="", year="", country="", borrowed=""):
        self.connection.cursor().execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR country=? OR borrowed=?",(title, author, year, country, borrowed))
        rows=self.connection.cursor().fetchall()
        return rows

    def delete(self, id):
        self.connection.cursor().execute("DELETE FROM books WHERE id=?",(id,))
        self.connection.commit()

    def update(self, id, title, author, year, country, borrowed):
        self.connection.cursor().execute("UPDATE books SET  title=?, author=?, year=?, country=?, borrowed=? WHERE id=?",(title, author, year, country, borrowed, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()



#connect()
#insert("john","khkhk","1988", "usa")
#print(view())
#print(search(title="john"))
#delete(3)
#update(id=2, title="cocomte3i")
#print(view())
