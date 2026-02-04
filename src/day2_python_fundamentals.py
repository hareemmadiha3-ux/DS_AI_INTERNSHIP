# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# User input

name = input("Enter your name: ")
age = int(input("Enter your current age: "))

age_2030 = age+4

print(f"Hey {name}, you will be {age_2030} years old in 2030.")
# Ask for total bill amount (float)
total_bill = float(input("Enter the total bill amount: "))

# Ask for number of people (int)
people = int(input("Enter the number of people: "))

# Calculate share per person
share_per_person = total_bill / people

# Print the result
print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")

# Bonus: Verify data types
print(type(total_bill))
print(type(people))
print(type(share_per_person))
# Hardcoded variables
item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True

# Print formatted details
print("Item:", item_name, 
      "Qty:", quantity, 
      "Price:", price, 
      "Available:", in_stock)

# Calculate total cost
total_cost = quantity * price

# Print total cost
print("Total Cost:", total_cost)