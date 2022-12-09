import sqlite3


def __main__():
    conn = sqlite3.connect("Final_database.db")
    cur = conn.cursor()
    table = (''' Create Table Final_database (Student_ID INTEGER PRIMARY KEY NOT NULL,
                                                 FirstName TEXT NOT NULL,
                                                 LastName TEXT,
                                                 Gender TEXT,
                                                 GraduationYear INT,
                                                 Major TEXT,
                                                 EmploymentStatus TEXT ''')

    cur.execute(''' INSERT INTO Final_Database (
                                       Student_ID,
                                       FirstName,
                                       LastName,
                                       Gender,
                                       GraduationYear,
                                       Major,
                                       EmploymentStatus)
                                       VALUES (1456, 'Bob', 'Johnson', 'Male', 2028, 'Computer Science', 'Full Time')''')

    print(table)
    conn.commit()
    conn.close()

