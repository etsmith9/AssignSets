#question2.py

# Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, 
# some of which are duplicated. Write a Python script to remove duplicates 
# and display the unique customer IDs.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
set_ids = set(customer_ids)
print(set_ids)