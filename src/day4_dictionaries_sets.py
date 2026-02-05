# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:56:05 2026

@author: Madiha
"""

contacts = {"Adeeba" : "9241079644", "Madiha" : "636048054", "sohail" : "9035018417"}
print(contacts)

#Add a new contact

contacts ["huda"] = "67997133086"
print(contacts)

#update an exisiting contacts phone number
contacts ["sohail"] = "9000000000"
print(contacts)

#safe access using.get()
existing_contacts = contacts.get("Adeeba", "contact not found")
missing_contacts = contacts.get("hareem", "contact not found")
print(contacts)

#print safe lookup results
print("Lookup Results:")
print("Adeeba:", existing_contacts)
print("hareem:", missing_contacts)

print("\n contacts List:")


# Iterate through dictionary and print all contacts
for name, phone in contacts.items():
    print(f"Contacts: {name} | Phone: {phone}")
    


#task 2
raw_logs =  ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]


# Convert list to a set to keep only unique IDs
unique_users = set(raw_logs)

# Membership test
check_id = "ID05" in unique_users

# Count comparison
original_count = len(raw_logs)
unique_count = len(unique_users)

# Output results
print("Unique User IDs:", unique_users)
print("Is ID05 present?", check_id)

print("\nCount Comparison:")
print("Original list count:", original_count)
print("Unique set count:", unique_count)


#task 3
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"} 

# Intersection: common interests
shared_interests = friend_a & friend_b

# Union: all unique interests
all_interests = friend_a | friend_b

# Difference: interests only friend_a has
unique_to_a = friend_a - friend_b

# Output results
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Unique to Friend A:", unique_to_a)
