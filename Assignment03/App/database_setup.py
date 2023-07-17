import sqlite3

conn = sqlite3.connect('student_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        dob TEXT,
        amount_due REAL
    )
''')

conn.commit()
cursor.close()
conn.close()
