# Scenario 2: List of route costs to check

# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers.
# How can you operationalize the route cost lookup problem?

# PSUEDOCODE
# 1. Read both lists (routes and phone numbers)
# 2. Iterate through the entire list of phone numbers
# 3. For each phone number, look for a match
# 4. If no match exists, remove the rightmost digit and reset until a match is found
# 5. Store the largest match as well as it's associted
# 
# IDEAS
# 1. Sort the lists?
# 2. Convert the list of routes into a dictionary?
# 3. Return as tuple? (Array of tuples w/ Binary Search)
# 4. Build a tree, w/ 10 Nodes (0-9) -- Each node points to an array with another more nodes

