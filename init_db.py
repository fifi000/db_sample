import sqlite3


conn = sqlite3.connect('university.db')
columns = [
    'id INTEGER PRIMARY KEY',
    'student_id_number VARCHAR NOT NULL UNIQUE',
    'first_name VARCHAR NOT NULL',
    'last_name VARCHAR NOT NULL',
]

try:
    conn.execute(f'CREATE TABLE students ({", ".join(columns)})')
except sqlite3.OperationalError:
    pass
