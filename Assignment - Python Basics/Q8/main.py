# Two Sets
s1 = {1, 3, 5, 7, 9}
s2 = {2, 4, 6, 7, 9}

# Union
print(f"Union of Two Sets : {s1.union(s2)}")

# Intersection 
print(f"Intersection of Two Sets : {s1.intersection(s2)}")

# Difference  
print(f"Difference between Two Sets : {s1.difference(s2)}")

# Add a new element to s1
s1.add(15)
print(f"S1 After Adding New Element : {s1}")

# Remove an existing element from s2
s2.remove(9)
print(f"S2 After Removing Existing Element : {s2}")

# Print both sets after the modifications
print(f"Set 1 : {s1}")
print(f"Set 2 : {s2}")

