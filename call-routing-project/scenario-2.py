# Scenario 2: List of route costs to check

# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers.
# How can you operationalize the route cost lookup problem?

# GOAL
# Returns a textfile of numbers w/ their associated values
#
# EXAMPLE OUTPUT
# +15124156620,0.04
# +14152345678,0.03
# +19876543210,0

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

import re
pattern = re.compile(r"(\+[\d]+),([\d.]+)")
group  = pattern.search(open('misc/route-test.txt', 'r').read())

# convert the text files that contain the numbers and routes into a list
def read_list(filename):
    return [line.strip() for line in open(filename)]

# create a list of phone numbers
phone_numbers = read_list('misc/phone-numbers-10000.txt')

# create a list of routes
routes = read_list('misc/route-costs-1000000.txt')

dict_of_routes = {}

for line in routes:
    group  = pattern.search(line)
    route_key = group.group(1)
    route_cost = group.group(2)
    if route_key not in dict_of_routes:
        dict_of_routes[route_key] = route_cost
    elif dict_of_routes[route_key] > route_cost:
        dict_of_routes[route_key] = route_cost
# print("Dictionary:\n")
# print(dict_of_routes)




def route_cost_to_check(number, routes):
    
    # for number in phone_numbers:
    cut_num = number
    while cut_num not in dict_of_routes and len(cut_num) > 1:
        cut_num = cut_num[:-1]
    
    if cut_num == '+':
        return print(f"{number},{0.00}")
    else:
        return print(f"{number},{dict_of_routes[cut_num]}")

for number in phone_numbers:
    route_cost_to_check(number, routes)

# route_cost_to_check(phone_numbers, routes)