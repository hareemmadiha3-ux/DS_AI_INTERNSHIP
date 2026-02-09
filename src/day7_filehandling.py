# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:34:34 2026

@author: Madiha"""
#task 1
name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily Goal: {goal}\n")

print("Saved successfully!")

#task 2
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    print("Students who passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
            
 #task 3           
try:
 
 
 with open("config.txt", 'r') as file: 
    content = file.read()
    print(content)

except FileNotFoundError: 
    print( "Oops! That file doesn't exist yet")      
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        