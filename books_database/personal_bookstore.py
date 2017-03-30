from tkinter import *

import backend



window = Tk()

window.wm_title("My Books")

def view_command():
	listbox.delete(0,END)
	for row in backend.view():
		listbox.insert(END, row)

def search_command():
	listbox.delete(0,END)
	for row in backend.search(title.get(),author.get(),year.get(),country.get()):
		listbox.insert(END, row)

def add_command():
	backend.insert(title.get(),author.get(),year.get(),country.get())
	listbox.delete(0,END)
	listbox.insert(END, (title.get() ,author.get() ,year.get() , country.get()))

def get_selected_row(event):
	index=listbox.curselection()[0] #return index of the row in form of a tuple (index,) hence the [0]
	global selected_tuple #global variable in order to be passed to the delete_command function
	selected_tuple=listbox.get(index)
	#fill entries with selected row
	e_title.delete(0,END)
	e_title.insert(END, selected_tuple[1])
	e_author.delete(0,END)
	e_author.insert(END, selected_tuple[2])
	e_year.delete(0,END)
	e_year.insert(END, selected_tuple[3])
	e_country.delete(0,END)
	e_country.insert(END, selected_tuple[4])

def delete_command():
	backend.delete(selected_tuple[0])
	listbox.delete(ANCHOR)
	e_title.delete(0,END)
	e_author.delete(0,END)
	e_year.delete(0,END)
	e_country.delete(0,END)

def update_command():
	backend.update(selected_tuple[0],title.get(),author.get(),year.get(),country.get())
	view_command()




#title
label_title=Label(window, text="Title")
label_title.grid(row=0, column=0)

title=StringVar()
e_title=Entry(window, textvariable=title)
e_title.grid(row=0,column=1)

#author
label_author=Label(window, text="Author")
label_author.grid(row=0, column=2)

author=StringVar()
e_author=Entry(window, textvariable=author)
e_author.grid(row=0,column=3)

#year
label_year=Label(window, text="Year")
label_year.grid(row=1, column=0)

year=StringVar()
e_year=Entry(window, textvariable=year)
e_year.grid(row=1,column=1)

#country
label_country=Label(window, text="Country")
label_country.grid(row=1, column=2)

country=StringVar()
e_country=Entry(window, textvariable=country)
e_country.grid(row=1,column=3)

#list box and attached scroll bar
listbox=Listbox(window, height=10, width=40)
listbox.grid(row=2, column=0, rowspan=6, columnspan=3)
	#get_selected_row function is triggered when user select an item in the listbox
listbox.bind("<<ListboxSelect>>", get_selected_row)

# scrollbar=Scrollbar(window)
# scrollbar.grid(row=2,column=2,rowspan=6)

# listbox.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=listbox.yview)

#actions

b_view=Button(window, text="View all", width=12, command=view_command)
b_view.grid(row=2, column=3)

b_search=Button(window, text="Search", width=12, command=search_command)
b_search.grid(row=3, column=3)

b_update=Button(window, text="Update", width=12)
b_update.grid(row=5, column=3)

b_add=Button(window, text="Add", width=12, command=add_command)
b_add.grid(row=4, column=3)

b_delete=Button(window, text="Delete", width=12, command=delete_command)
b_delete.grid(row=5, column=3)

b_delete=Button(window, text="Update", width=12, command=update_command)
b_delete.grid(row=6, column=3)

#b_close=Button(window, text="Close", width=12, command=window.destroy)
#b_close.grid(row=7, column=3)


window.mainloop()