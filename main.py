import sqlite3

connect=sqlite3.connect("student.db")

c=connect.cursor()

username=input("Enter Username:")
password=input("Enter Password:")

c.execute(f'''

SELECT * from users where username='{username}' AND password='{password}'

''')

print(c.fetchone())

connect.commit()
connect.close()