from tkinter import \
    ACTIVE, ANCHOR, END, Label, StringVar, Entry, Button, Listbox, Tk

from backend import Database

database = Database("books.db")


class BookEntry:

    def __init__(self, label, window, position):
        self.window = window
        self.row, self.column = position

        self.set_label(label)
        self.set_entry()

    def set_entry(self):
        self.value = StringVar()
        self.entry = Entry(window, textvariable=self.value)
        self.entry.grid(row=self.row, column=self.column + 1)

    def set_label(self, name):
        self.label = Label(self.window, text=name)
        self.label.grid(row=self.row, column=self.column)

    def set(self, value):
        self.value.set(value)

    def clear(self):
        self.set('')

    def get(self):
        return self.value.get()


class Window:

    def __init__(self, window):
        self.window = window
        self.window.wm_title("My Books")

        self.title = BookEntry("Title", window, (0, 0))
        self.author = BookEntry("Author", window, (0, 2))
        self.year = BookEntry("Year", window, (1, 0))
        self.country = BookEntry("Country", window, (1, 2))
        self.borrowed = BookEntry("Borrowed", window, (2, 0))

        self.make_button("View all", 12, self.view, (3, 3))
        self.make_button("Search", 12, self.search, (4, 3))
        self.make_button("Add", 12, self.add, (5, 3))
        self.make_button("Update", 12, self.add, (6, 3))
        self.make_button("Delete", 12, self.delete, (7, 3))

        self.books = Listbox(window, height=10, width=40)
        self.books.grid(row=3, column=0, rowspan=6, columnspan=3)
        # select_row is called when user select an item in the listbox
        self.books.bind("<<ListboxSelect>>", self.select_row)

    def make_button(self, text, width, callback, position):
        b = Button(self.window, text=text, width=width, command=callback)
        b.grid(row=position[0], column=position[1])

    # Callbacks:
    def delete(self):
        """
        Delete the book corresponding to the active row
        """
        book_id = self.books.get(self.books.curselection())[0]
        database.delete(book_id)
        self.view()

    def update(self):
        """
        Update the book corresponding to the active row with the current data
        """
        row = self.books.get(ACTIVE)
        database.update(*row)
        self.view_command()

    def view(self):
        """
        Retrieve the whole list of books, and display it.
        """
        books = database.view()
        self.show_books(books)

    def search(self):
        """
        Retrieve the list of books that match the current input, and display
        it.
        """
        books = database.search(*self.get_input())
        self.show_books(books)

    def add(self):
        """
        Create a new book entry in the database from the current input and
        refresh the list of books.
        """
        entries = self.get_input()
        database.insert(*entries)
        self.view()

    def show_books(self, books):
        """
        Populate the book list with the given books
        """
        self.books.delete(0, END)
        for book in books:
            self.books.insert(END, book)

    def select_row(self, event):
        """
        Populate the input fields with the row currently selected
        """
        row = self.books.get(self.books.curselection())
        print(row)
        self.set_input(*list(row)[1:])

    def get_input(self):
        return (
            self.title.get(),
            self.author.get(),
            self.year.get(),
            self.country.get(),
            self.borrowed.get())

    def set_input(self, title, author, year, country, borrowed):
        self.title.set(title)
        self.author.set(author)
        self.year.set(year)
        self.country.set(country)
        self.borrowed.set(borrowed)

    def clear_input(self):
        self.title.clear()
        self.author.clear()
        self.year.clear()
        self.country.clear()
        self.borrowed.clear()


window = Tk()
Window(window)
window.mainloop()
