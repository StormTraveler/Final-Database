from tkinter import ttk

import tkinter as tk

import sqlite3

def connect():

    con1 = sqlite3.connect("Final_Database.db")

    cur1 = con1.cursor()

    cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

    con1.commit()

    con1.close()


def View():

    con1 = sqlite3.connect("Final_Database.db")

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM Students")

    rows = cur1.fetchall()

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:

        print(row)

        tree.insert("", tk.END, values=row)

    con1.close()


def Insert():
    con1 = sqlite3.connect("Final_Database.db")
    cur1 = con1.cursor()

    input = Entry.get()
    list = input.split()
    print(list)
    cur1.executemany(''' INSERT INTO Students 
    (ID, FirstName, LastName, Gender, GraduationYear,Major, EmploymentStatus) VALUES(?, ?, ?, ?, ?, ?, ?)''', (list,))

    con1.commit()
    con1.close()
    # connect to the database


def Delete():
    con1 = sqlite3.connect("Final_Database.db")
    cur1 = con1.cursor()

    row = int(Entry.get())

    print(row)
    cur1.execute("DELETE FROM Students WHERE ID = ?", (row,))

    con1.commit()
    con1.close()

connect()

root = tk.Tk()


tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="First Name")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="Last Name")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="Gender")

tree.column("#5", anchor=tk.CENTER)

tree.heading("#5", text="GraduationYear")

tree.column("#6", anchor=tk.CENTER)

tree.heading("#6", text="Major")

tree.column("#7", anchor=tk.CENTER)

tree.heading("#7", text="EmploymentStatus")

tree.pack()

button1 = tk.Button(text="Display data", command=View)

button1.pack(pady=10)

button2 = tk.Button(text="Insert Data", command=Insert)

button2.pack()

button3 = tk.Button(text="Delete Data", command=Delete)

button3.pack()

# button3 = tk.Button(text="Delete Data", command=Delete)

Entry = tk.Entry(width=100)

Entry.pack(pady=10)

View() # Show initial Data Table
root.mainloop()
