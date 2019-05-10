# Scenario 1: One-time route cost check

# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number.
# How quickly can you find the cost of calling this number?

# ANSWER:
# Based on your desired operating system:
# Use CTRL + F (Windows/Linux) or ⌘ + F (OSX) in your text-editor of choice
# You search for the phone number itself and find the price associated with it


# ALTERNATIVE ANSWER:
# In UNIX you can use GREP to search plain-text data sets for lines that match the regular expression
# GREP utilizes Boyer-Moore's string-search algorithm
# Boyer-Moore's string-search algorithm has a
# Preprocessing Time of: Θ(m + k)	
# Matching Time of: Ω(n/m) in the best case and O(mn) in the worst case
# Space: Θ(k)