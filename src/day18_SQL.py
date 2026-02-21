# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 23:20:37 2026

@author: Madiha
"""
#Task 1
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("internship.db")

# Write JOIN query
query = """
SELECT interns.name, interns.track, mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

# Execute query and load into DataFrame
df = pd.read_sql_query(query, conn)

# Print result
print(df)

# Close connection
conn.close()

#Task 2
import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")

# Filter Query
filter_query = """
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000;
"""
df_filter = pd.read_sql_query(filter_query, conn)
print("Filtered Interns:")
print(df_filter)

# Average Stipend
avg_query = """
SELECT track, AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track;
"""
df_avg = pd.read_sql_query(avg_query, conn)
print("\nAverage Stipend Per Track:")
print(df_avg)

# Count Interns
count_query = """
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""
df_count = pd.read_sql_query(count_query, conn)
print("\nIntern Count Per Track:")
print(df_count)

conn.close()