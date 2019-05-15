#!python

import re

PATTERN = re.compile(r"(\+[\d]+),([\d.]+)")

def text_to_list(text):
    '''Returns a list of lines in a given text file'''
    return [line.strip() for line in open(text)]

def parse_routes(routes_file):
    '''Returns an iterable object of phone numbers with corresponding
    prices for a call to the number.'''
    text = text_to_list(routes_file)
    for line in text:
        match = PATTERN.search(line)
        number = match.group(1)
        price = match.group(2)
        yield (number, price)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        # Price doubles as flag for end of a pattern
        self.price = None

    def __repr__(self):
        """Return a string representation of this trie node."""
        return 'TrieNode()'

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.children == {}

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return not self.is_leaf()

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        # Nodes without children have no height
        if self.is_leaf():
            return 0

        heights = []
        
        # Check on every possible child if it exists
        for child in self.children:
            # Measure the height of the child and
            # add height to the list of heights
            heights.append(self.children[child].height())

        # Return the height of the tallest child + 1 for current node
        return max(heights) + 1


class RouterTrie(object):
    def __init__(self, numbers_file='', costs_file=''):
        ''' Initialize decimal trie'''
        self.root = TrieNode()
        self.size = 0

    def __repr__(self):
        '''Return a string representation of the trie'''
        return f'RouterTrie({self.size})'

    def is_empty(self):
        '''Returns True if the the trie has no nodes'''
        return self.root == None

    def height(self):
        '''Returns the height of this trie (the number of edges on the longest
        downward path from this trie's root node to a descendant leaf node).'''
        if self.root:
            return self.root.height()
        return None
    
    def find_price(self, number):
        '''Returns the price of a call to a given phone number'''
        node = self.root
        # Iterate through characters in a phone number
        for elem in number:
            # Break if number not in trie
            if elem not in node.children:
                return 0
            # Move down trie as you read right on number
            node = node.children[elem]
        # Return price if it exists
        if node.price:
            return node.price
        return 0
    
    def insert(self, number, price):
        '''Inserts a price to a call if there is none or if the new price is
        cheaper than the existing price.'''
        node = self.root
        # Iterate through characters in phone number
        for elem in number:
            # Create nodes for characters if not there
            if elem not in node.children:
                node.children[elem] = TrieNode()
            # Move down trie as you read right on number
            node = node.children[elem]
        # Set price at end of the number if not there
        if not node.price:
            node.price = price
        # Or if the new price is smaller
        elif node.price > price:
            node.price = price
    

if __name__ == "__main__":
    # import sys
    # args = sys.argv[1:]

    # text = parse_routes(args[0])
    # print(list(text))
    #============NODE CLASS============#
    node = TrieNode()
    children = ['0', '1', '2', '3']
    for c in children:
        node.children[c] = TrieNode()
    print(node.is_leaf())
    print(node.children)
    print(node.height())