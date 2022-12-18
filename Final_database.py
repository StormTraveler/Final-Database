from tkinter import ttk

import tkinter as tk

import sqlite3

def connect():

    con1 = sqlite3.connect("Final_Database.db")

    cur1 = con1.cursor()

    cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")

    con1.commit()

    con1.close()


def Refresh():

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
    Refresh()
    con1.close()
    # connect to the database


def Edit():
    con1 = sqlite3.connect("Final_Database.db")
    cur1 = con1.cursor()

    inp = Entry.get()
    inp = inp.split()

    print(inp)
    if inp[0] == "FirstName":
        cur1.execute("UPDATE Students SET FirstName = ? where id = ? ", (inp[2], inp[1]))
    if inp[0] == "LastName":
        cur1.execute("UPDATE Students SET LastName = ? where id = ? ", (inp[2], inp[1]))
    if inp[0] == "Gender":
        cur1.execute("UPDATE Students SET Gender = ? where id = ? ", (inp[2], inp[1]))
    if inp[0] == "GraduationYear":
        cur1.execute("UPDATE Students SET GraduationYear = ? where id = ? ", (inp[2], inp[1]))
    if inp[0] == "Major":
        cur1.execute("UPDATE Students SET Major = ? where id = ? ", (inp[2], inp[1]))
    if inp[0] == "EmploymentStatus":
        cur1.execute("UPDATE Students SET EmploymentStatus = ? where id = ? ", (inp[2], inp[1]))

    con1.commit()
    Refresh()
    con1.close()


def Delete():
    con1 = sqlite3.connect("Final_Database.db")
    cur1 = con1.cursor()

    row = int(Entry.get())

    print(row)
    cur1.execute("DELETE FROM Students WHERE ID = ?", (row,))

    con1.commit()
    Refresh()
    con1.close()

connect()

root = tk.Tk()


for i in range(1): # This is only here so that I can minimize it
    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="ID")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="FirstName")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="LastName")

    tree.column("#4", anchor=tk.CENTER)

    tree.heading("#4", text="Gender")

    tree.column("#5", anchor=tk.CENTER)

    tree.heading("#5", text="GraduationYear")

    tree.column("#6", anchor=tk.CENTER)

    tree.heading("#6", text="Major")

    tree.column("#7", anchor=tk.CENTER)

    tree.heading("#7", text="EmploymentStatus")

    tree.pack()

    button1 = tk.Button(text="Refresh Data", command=Refresh)

    button1.pack(pady=10)

    button2 = tk.Button(text="Insert Data", command=Insert)

    button2.pack()

    button3 = tk.Button(text="Delete Data", command=Delete)

    button3.pack()

    button4 = tk.Button(text="Edit Data", command=Edit)

    button4.pack()

# button3 = tk.Button(text="Delete Data", command=Delete)

Entry = tk.Entry(width=100)

Entry.pack(pady=10)

Refresh() # Show initial Data Table
root.mainloop()
