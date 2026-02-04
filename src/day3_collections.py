# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:50:32 2026

@author: Madiha
"""

#task 1
inventory = ["apple","banana","carrot","dates"]
print(inventory)
inventory.append("eggs")
print(inventory)
inventory.remove("banana")
print(inventory)

# Temperature readings recorded every hour
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

# First and last readings
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])

# Afternoon Peak (4th, 5th, and 6th items)
afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)

# Last 3 hours
last_3_hours = temperatures[-3:]
print("Last 3 Hours Readings:", last_3_hours)

# Create a tuple for screen resolution
screen_res = (1920, 1080)

# Print the current resolution
print("Current Resolution:", screen_res[0], "x", screen_res[1])

# ❌ Experiment: Trying to change the width
# screen_res[0] = 1280   # This will cause a TypeError

# ✅ Fix
print("Tuples cannot be modified!")

