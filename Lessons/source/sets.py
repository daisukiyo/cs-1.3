#!python

# this implementation of the Set class is backed by hash tables
from hashtable import HashTable

class Sets(object):
    
    def __init__(self, elements=None):
        # initialize a new empty set structure, and add each element if a sequence is given
        self.set_struct = HashTable()

        if elements is not None: 
            for values in elements:
                if not self.contains(values):
                    self.add(values)

    def size(self):
        # property that tracks the number of elements in constant time
        return self.set_struct.size()

    def contains(self, element):
        # return a boolean indicating whether element is in this set
        return self.set_struct.contains(element)

    def add(self, element):
        # add element to this set, if not present already
        return self.set_struct.set(element, value=None)

    def remove(self, element):
        # remove element from this set, if present, or else raise KeyError
        return self.set_struct.delete(element)

        # if element in self.set_struct:
        #     self.set_struct.delete(element)
        #     return
        # raise KeyError('element not present in set: {}'.format(self.set_struct))
    
    def union(self, other_set):
        # return a new set that is the union of this set and other_set
        union = Sets()
        for item in self.set_struct.keys():
            union.add(item)
        
        for item in other_set.set_struct.keys():
            union.add(item)

        return union
    
    def intersection(self, other_set):
        # return a new set that is the intersection of this set and other_set
        intersection = Sets()

        if other_set.size() > self.size():
            larger_set = other_set
            smaller_set = self
        else:
            larger_set = self
            smaller_set = other_set

        for item in smaller_set.hash_set.keys():
            if larger_set.contains(item):
                intersection.add(item)

        return intersection
            

    def difference(self, other_set):
        # return a new set that is the difference of this set and other_set
        difference = Sets()

        for item in self.set_struct.keys():

            if other_set.contains(item):
                continue

            difference.add(item)

        return difference

    def is_subset(self, other_set):
        # return a boolean indicating whether other_set is a subset of this set
        if other_set.size() > self.size():
            return False
        
        is_subset = True
        
        for item in other_set.set_struct.keys():
            if not self.contains(item):
                is_subset = False
        return is_subset