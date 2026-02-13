# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 10:36:56 2026

@author: Madiha
"""

import pandas as pd

# Create the altered dataset
data = {
    "CustomerID": [201,202,203,204,205,206,207,207,208,209],
    "Name": ["Aman","Sana","Rohit",None,"Pooja","Daniel","Meera","Meera","Arif","Ritu"],
    "Age": [24,None,31,23,None,29,36,36,None,27],
    "City": ["Bangalore "," Mumbai","Delhi",None,"Bangalore","Chennai","Mumbai","Mumbai","Delhi","Bangalore"],
    "OrderAmount": [2600,1750,None,2100,3200,None,1400,1400,2800,None],
    "PaymentMethod": ["UPI","Card","Cash","Card",None,"UPI","Cash","Cash","Card","UPI"],
    "Date": ["2024-01-06","2024-01-12","2024-02-03","2024-02-06","2024-03-02",
             "2024-03-06","2024-03-12","2024-03-12","2024-04-03","2024-04-07"]
}

# Load into DataFrame
df = pd.DataFrame(data)

# Shape BEFORE cleaning
print("Shape before cleaning:", df.shape)

# Report missing values
print("\nMissing values per column:")
print(df.isna().sum())

# Fill missing numeric values with MEDIAN
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Shape AFTER cleaning
print("\nShape after cleaning:", df.shape)


#task 2


import pandas as pd

# Sample dataset where Price is stored as text and Date as object
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "Price": ["$1200", "$800", "$450", "$300"],
    "Date": ["2024-01-05", "2024-02-10", "2024-03-15", "2024-04-20"]
}

df = pd.DataFrame(data)

# STEP 1: Check initial data types
print("Data types BEFORE conversion:\n")
print(df.dtypes)

# STEP 2: Remove '$' symbol and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# STEP 3: Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check data types after conversion
print("\nData types AFTER conversion:\n")
print(df.dtypes)

#Task 3

import pandas as pd

# Sample dataset with inconsistent Location text
data = {
    "Location": [" New York", "new york", "NEW YORK ", " New york ", "Los Angeles", " los angeles "]
}

df = pd.DataFrame(data)

# Check unique values BEFORE cleaning
print("Unique values before cleaning:")
print(df["Location"].unique())

# STEP 1: Remove leading/trailing spaces
df["Location"] = df["Location"].str.strip()

# STEP 2: Standardize casing (choose one: title or lower)
df["Location"] = df["Location"].str.title()

# STEP 3: Verify fix
print("\nUnique values after cleaning:")
print(df["Location"].unique())
