# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:04:43 2026

@author: Madiha
"""
import pandas as pd

products = pd.Series([700,150,300], index = ("laptop","mouse","keyboard"))
print(products)

#access the price of laptop
print(products["laptop"])

#slicing the first two products
first_two = products.iloc[0:2]
print(first_two)


#task 2
import pandas as pd

grades = pd.Series ([85, None, 92, 45, None, 78, 55])
print(grades)

#identifying null values
print(grades.isnull())

print(grades.fillna(0))

print(grades[grades > 60])


#task 3
import pandas as pd

# Create the Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Step 1 & 2: Clean the text
cleaned = usernames.str.strip().str.lower()

# Step 3: Check for letter 'a'
has_a = cleaned.str.contains('a')

print("Cleaned usernames:")
print(cleaned)

print("\nContains letter 'a':")
print(has_a)
