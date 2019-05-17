# Scenario 2: List of route costs to check

# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a list of 1000 phone numbers.
# How can you operationalize the route cost lookup problem?

# GOAL
# Returns a textfile of numbers w/ their associated values

# EXAMPLE OUTPUT
# +15124156620,0.04
# +14152345678,0.03
# +19876543210,0

# PSUEDOCODE
# 1. Read both lists (routes and phone numbers)
# 2. Iterate through the entire list of phone numbers
# 3. For each phone number, look for a match
# 4. If no match exists, remove the rightmost digit and reset until a match is found
# 5. Store the largest match as well as it's associted cost

# POTENTIAL IDEAS
# 1. Sort the lists?
# 2. Convert the list of routes into a dictionary?
# 3. Return as tuple? (Array of tuples w/ Binary Search)
# 4. Build a tree, w/ 10 Nodes (0-9) -- Each node points to an array with another more nodes

# used for benchmarking
import time
# import regular expressions
import re
# create a pattern to be used for matching
pattern = re.compile(r"(\+[\d]+),([\d.]+)")
# read a textfile to find matches
match  = pattern.search(open('misc/route-costs-1000000.txt', 'r').read())

# parse through ever route in the file (sets up our dictionary)
def populate_dictionary(routes):
    for line in routes:
        # match every line to the given pattern
        match = pattern.search(line)
        # translates the left half of the line as a key (route)
        route_key = match.group(1)
        # translates the right half of the line as a value (cost)
        route_cost = match.group(2)

        # assign as cost if matched, or take a lower cost if present
        if route_key not in dict_of_routes:
            dict_of_routes[route_key] = route_cost
        elif dict_of_routes[route_key] > route_cost:
            dict_of_routes[route_key] = route_cost

def route_cost_to_check(number, routes):
    # for number in phone_numbers:
    cut_num = number

    # decrement the phone number until their is a matching route
    while cut_num not in dict_of_routes and len(cut_num) > 1:
        cut_num = cut_num[:-1]
    
    # return a cost of 0 when there isn't a matching route, otherwise return the associated cost
    if cut_num == '+':
        return f"{number},{0}\n"
    else:
        return f"{number},{dict_of_routes[cut_num]}\n"

# convert the text files that contain the numbers and routes into a list
def read_list(filename):
    return [line.strip() for line in open(filename)]

# create a list of phone numbers
phone_numbers = read_list('misc/phone-numbers-10000.txt')

# create a list of routes
routes_list = read_list('misc/route-costs-10000000.txt')

dict_of_routes = {}

# begin timer
current = time.perf_counter()

# populate dictionary
populate_dictionary(routes_list)

# Returns runtime in (seconds)
print(f'Buildtime: {time.perf_counter() - current}')

print("Results Recorded: 'scenario-2-results.txt'")
# outputs the results into a textfile
result = open('scenario-2-results.txt', 'w')
for number in phone_numbers:
    result.write(route_cost_to_check(number, routes_list))
result.close()
