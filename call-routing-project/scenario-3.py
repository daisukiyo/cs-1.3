#!python

import re

PATTERN = re.compile(r"(\+[\d]+),([\d.]+)")

def text_to_list(self, text):
    return [line.strip() for line in open(text)]

def _parse_routes(self, routes_file):
    for line in self.text_to_list(routes_file):
        match = PATTERN.search(line)
        number = match.group(1)
        price = match.group(2)
    


class TrieNode(object):
    def __init__(self, data):
        self.data = data
        self.children = [None] * 10
        self.price = None

    def __repr__(self):
        """Return a string representation of this trie node."""
        return f'TrieNode({self.data})'

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.children == [None] * 10

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return not self.is_leaf()

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        # Nodes without children have no height
        if self.is_leaf:
            return 0

        heights = []
        
        # Check on every possible child if it exists
        for child in self.children:
            if child is not None:
                # Measure the height of the child and
                # add height to the list of heights
                heights.append(child.height())

        # Return the height of the tallest child + 1 for current node
        return max(heights) + 1


class RouterTrie(object):
    def __init__(self, numbers_file='', costs_file=''):
        self.root = TrieNode('+')
        self.size = 0

    def __repr__(self):
        return f'RouterTrie({self.size})'

    def is_empty(self):
        return self.root == None

    def height(self):
        if self.root:
            return self.root.height()
        return None

    def contains(self, number):
        return self.search(number) is not None

    def search(self, number):
        return None

    def insert(self, number, price):
        pass
    
    def _find_parent(self):
        pass

if __name__ == "__main__":
    pass