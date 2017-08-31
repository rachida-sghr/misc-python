import sqlite3


class Database:

    def __init__(self, database):
        self.con=sqlite3.connect("books.db")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRiMARY KEY , title TEXT, author TEXT, year INTEGER, country TEXT, borrowed TEXT)")
        self.con.commit()

    def insert(self, title, author, year, country, borrowed):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?,?)",(title, author, year, country, borrowed))
        self.con.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books")
        rows=self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", country="", borrowed=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR country=? OR borrowed=?",(title, author, year, country, borrowed))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?",(id,))
        self.con.commit()

    def update(self, id, title, author, year, country, borrowed):
        self.cur.execute("UPDATE books SET  title=?, author=?, year=?, country=?, borrowed=? WHERE id=?",(title, author, year, country, borrowed, id))
        self.con.commit()

    def __del__(self):
        self.con.close()



#connect()
#insert("john","khkhk","1988", "usa")
#print(view())
#print(search(title="john"))
#delete(3)
#update(id=2, title="cocomte3i")
#print(view())
