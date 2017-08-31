from tkinter import \
    ACTIVE, ANCHOR, END, Label, StringVar, Entry, Button, Listbox, Tk

from backend import Database

database = Database("books.db")


class Window:

    def __init__(self, window):
        self.window = window
        self.window.wm_title("My Books")

        # title
        label_title = Label(window, text="Title")
        label_title.grid(row=0, column=0)

        self.title = StringVar()
        self.e_title = Entry(window, textvariable=self.title)
        self.e_title.grid(row=0, column=1)

        # author
        label_author = Label(window, text="Author")
        label_author.grid(row=0, column=2)

        self.author = StringVar()
        self.e_author = Entry(window, textvariable=self.author)
        self.e_author.grid(row=0, column=3)

        # year
        label_year = Label(window, text="Year")
        label_year.grid(row=1, column=0)

        self.year = StringVar()
        self.e_year = Entry(window, textvariable=self.year)
        self.e_year.grid(row=1, column=1)

        # country
        label_country = Label(window, text="Country")
        label_country.grid(row=1, column=2)

        self.country = StringVar()
        self.e_country = Entry(window, textvariable=self.country)
        self.e_country.grid(row=1, column=3)

        # borrowed
        label_borrowed = Label(window, text="Borrowed")
        label_borrowed.grid(row=2, column=0)

        self.borrowed = StringVar()
        self.e_borrowed = Entry(window, textvariable=self.borrowed)
        self.e_borrowed.grid(row=2, column=1)

        # list box and attached scroll bar
        self.listbox = Listbox(window, height=10, width=40)
        self.listbox.grid(row=3, column=0, rowspan=6, columnspan=3)
        # get_selected_row function is triggered when user select an item in
        # the listbox
        self.listbox.bind("<<ListboxSelect>>", self.get_selected_row)

        # scrollbar = Scrollbar(window)
        # scrollbar.grid(row=2, column=2, rowspan=6)

        # listbox.configure(yscrollcommand=scrollbar.set)
        # scrollbar.configure(command=listbox.yview)

        # buttons

        b_view = Button(window, text="View all", width=12, command=self.view_command)
        b_view.grid(row=3, column=3)

        b_search = Button(window, text="Search", width=12, command=self.search_command)
        b_search.grid(row=4, column=3)

        b_add = Button(window, text="Add", width=12, command=self.add_command)
        b_add.grid(row=5, column=3)

        b_update = Button(window, text="Update", width=12, command=self.update_command)
        b_update.grid(row=6, column=3)

        b_delete = Button(window, text="Delete", width=12, command=self.delete_command)
        b_delete.grid(row=7, column=3)

    def view_command(self):
        self.listbox.delete(0, END)
        for row in database.view():
            self.listbox.insert(END, row)

    def search_command(self):
        self.listbox.delete(0, END)
        for row in database.search(self.title.get(), self.author.get(), self.year.get(), self.country.get(), self.borrowed.get()):
            self.listbox.insert(END, row)

    def add_command(self):
        database.insert(self.title.get(), self.author.get(), self.year.get(), self.country.get(), self.borrowed.get())
        self.listbox.delete(0, END)
        self.listbox.insert(END, (self.title.get(), self.author.get(), self.year.get(), self.country.get(), self.borrowed.get()))

    def get_selected_row(self, event):
        entry = self.listbox.get(ACTIVE)
        self.populate_entries(*entry)

    def populate_entries(self, title, author, year, country, borrowed):
        self.e_title.delete(0, END)
        self.e_title.insert(END, title)

        self.e_author.delete(0, END)
        self.e_author.insert(END, author)

        self.e_year.delete(0, END)
        self.e_year.insert(END, year)

        self.e_country.delete(0, END)
        self.e_country.insert(END, country)

        self.e_borrowed.delete(0, END)
        self.e_borrowed.insert(END, borrowed)

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.listbox.delete(ANCHOR)
        self.e_title.delete(0, END)
        self.e_author.delete(0, END)
        self.e_year.delete(0, END)
        self.e_country.delete(0, END)
        self.e_borrowed.delete(0, END)

    def update_command(self):
        database.update(self.selected_tuple[0], self.title.get(), self.author.get(), self.year.get(), self.country.get(), self.borrowed.get())
        self.view_command()


window = Tk()
Window(window)
window.mainloop()
