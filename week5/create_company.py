import sqlite3
import os

database = sqlite3.connect(':memory:')
database_name = "company_database"
database = sqlite3. connect(database_name)
cursor = database.cursor()


cursor.execute('''CREATE TABLE company(id INTEGER PRIMARY KEY, name TEXT, montly_salary INTEGER, yearly_bonus INTEGER, position TEXT)''')
database.commit()

company_data = [("Ivan Ivanov", 5000, 10000, "Software Engineer"), ("Rado Rado", 500, 0, "Technical Support Intern"), ("Ivo Ivo", 10000, 100000, "CEO"), ("Petar Petrov", 3000, 1000, "Marketing Manager"), ("Maria Georgieva", 8000, 10000, "COO")]
cursor.executemany('''INSERT INTO company(name, montly_salary, yearly_bonus, position)VALUES(?,?,?,?)''', company_data)
print('All users inserted')
database.commit()
