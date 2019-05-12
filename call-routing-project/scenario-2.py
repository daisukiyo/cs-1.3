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

# convert the text files that contain the numbers and routes into a list
def read_list(filename):
    return [line.strip() for line in open(filename)]

# create a list of phone numbers
phone_numbers = read_list('misc/phone-test.txt')

# create a list of routes
routes = read_list('misc/route-test.txt')

# create a list for the final output
cost_lookup = []

costs = []

def route_cost_to_check(phone_numbers, routes):
    for number in phone_numbers:
        # create variable to keep track of phones w/ matching routes
        print(number)
        reduced_number = number
        for route in routes:
            print(route)
   
            while reduced_number not in route and len(reduced_number) > 1:
                # print(reduced_number)
                reduced_number = reduced_number[:-1]

            if len(reduced_number) != 0:
                # costs.append(route)

                # print(reduced_number)
                # print(route[-5:])
                match_with_cost = (number + route[-5:])

                cost_lookup.append(match_with_cost)
                # number += route[-5:]
                # cost_lookup.append(number)

            else:
                continue
    
    # print(cost_lookup)

# route_cost_to_check(phone_numbers, routes)

def kms(phone_numbers, routes):
    for number in phone_numbers:
        for route in routes:
            while number not in route and len(number) != 2:
                number = number[:-1]
            
            print(number)
                
kms(phone_numbers, routes)