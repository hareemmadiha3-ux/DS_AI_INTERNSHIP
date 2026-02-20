# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:55:13 2026

@author: Madiha
"""

import sqlite3

# Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Insert data
intern_data = [
    ('madiha', 'Data Science', 15000),
    ('Hareem', 'Web Dev', 25000),
    ('huda', 'Robotics', 10000),
    ('huda', 'Robotics', 10000),
    ('Anas', 'Data Science', 30000)
]

cursor.executemany("INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)", intern_data)

conn.commit()

# Query specific columns
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

conn.close()