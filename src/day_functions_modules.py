# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:40:57 2026

@author: Madiha
"""

# Function to calculate area and perimeter
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (12 +6)
    return area, perimeter   # returning as a tuple

   # Taking user input
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

# Calling the function
area, perimeter = calc_rectangle(length, width)

# Printing the result
print(f"Area: {area}, Perimeter: {perimeter}")

