import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect("my_database.db")
curr = conn.cursor()
curr.execute("DROP TABLE IF EXISTS student")

curr.execute("""
CREATE TABLE student (
    stu_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    stu_name TEXT NOT NULL, 
    stu_course TEXT NOT NULL
)
""")
conn.commit()

curr.execute("""INSERT INTO student (stu_name, stu_course) VALUES 
    ('Ravi', 'Mech'), 
    ('Yash', 'Civil');
    """
)

    
conn.commit()

curr.execute("SELECT * FROM student")
rows = curr.fetchall()
table = PrettyTable(["ID","Name","Course"])
for row in rows:
    table.add_row(row)
print(table)

print("Table 'student' has been recreated!")


