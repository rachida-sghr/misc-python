import sqlite3

def connect():
	con=sqlite3.connect("books.db")
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRiMARY KEY , title TEXT, author TEXT, year INTEGER, country TEXT)")
	con.commit()
	con.close()

def insert(title, author, year, country):
	con=sqlite3.connect("books.db")
	cur=con.cursor()
	cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title, author, year, country))
	con.commit()
	con.close()

def view():
	con=sqlite3.connect("books.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM books")
	rows=cur.fetchall()
	con.close()
	return rows

def search(title="", author="", year="", country=""):
	con=sqlite3.connect("books.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR country=?",(title, author, year, country))
	rows=cur.fetchall()
	con.close()
	return rows

def delete(id):
	con=sqlite3.connect("books.db")
	cur=con.cursor()
	cur.execute("DELETE FROM books WHERE id=?",(id,))
	con.commit()
	con.close()

def update(id, title, author, year, country):
	con=sqlite3.connect("books.db")
	cur=con.cursor()
	cur.execute("UPDATE books SET  title=?, author=?, year=?, country=? WHERE id=?",(title, author, year, country,id))
	con.commit()
	con.close()



#connect()
#insert("john","khkhk","1988", "usa")
print(view())
#print(search(title="john"))
#delete(3)
#update(id=2, title="cocomte3i")
#print(view())
