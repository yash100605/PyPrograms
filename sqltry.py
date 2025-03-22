import sqlite3
from prettytable import PrettyTable
while(True):
    conn = sqlite3.connect("my_database.db")
    curr = conn.cursor()
    curr.execute("""
    CREATE TABLE IF NOT EXISTS student (
        stu_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        stu_name TEXT NOT NULL, 
        stu_course TEXT NOT NULL
        )
    """)
    conn.commit()
    stu_name = input("Enter Name:")
    stu_course = input("Enter Course:")

    curr.execute("INSERT INTO student(stu_name,stu_course) VALUES (?,?)",(stu_name,stu_course))

    
    conn.commit()

    curr.execute("SELECT * FROM student")
    rows = curr.fetchall()
    table = PrettyTable(["ID","Name","Course"])
    for row in rows:
        table.add_row(row)
    print(table)

    print("Table 'student' has been recreated!")


