import unittest

from sets import Sets

class SetsTest(unittest.TestCase):

    def test_init(self):
        s = Sets()
        assert s.set_struct.size == 0

    def test_size(self):
        s = Sets()
        assert s.set_struct.size == 0
        s.add('A')
        assert s.set_struct.size == 1
        s.add('B')
        assert s.set_struct.size == 2
        s.add('C')
        assert s.set_struct.size == 3

    def test_contains(self):
        s = Sets(['A', 'B', 'C'])
        assert s.contains('A') == True
        assert s.contains('B') == True
        assert s.contains('C') == True
        assert s.contains('X') == False

    def test_add(self):
        s = Sets()
        s.add('A')
        assert s.set_struct.size == 1
        assert s.contains('A')
        s.add('A')
        assert s.set_struct.size == 1

        s.add('B')
        assert s.set_struct.size == 2
        assert s.contains('B')
        s.add('B')
        assert s.set_struct.size == 2

    def test_remove(self):
        s = Sets(['A', 'B', 'C'])
        assert s.set_struct.size == 3
        assert s.contains('A')
        assert s.contains('B')
        assert s.contains('C')

        s.remove('A')
        assert s.set_struct.size == 2
        assert s.contains('B')
        assert s.contains('C')

        s.remove('B')
        assert s.set_struct.size == 1
        assert s.contains('C')

        with self.assertRaises(KeyError):
            s.remove('A')
    
    def test_union(self):
        s1 = Sets(['A', 'B', 'C'])
        s2 = Sets(['D', 'E'])
        union_set = s1.union(s2)
        self.assertCountEqual(union_set.set_struct.keys(), ['A', 'B', 'C', 'D', 'E'])

        s1 = Sets(['A', 'A', 'B', 'C'])
        s2 = Sets(['E', 'F', 'G'])
        union_set = s1.union(s2)
        assert (union_set.set_struct.size == 7) == False
    
    def test_intersection(self):
        s1 = Sets(['A', 'B', 'C'])
        s2 = Sets(['A', 'B', 'D'])
        intersection_set = s1.intersection(s2)
        self.assertCountEqual(intersection_set.set_struct.keys(), ['A', 'B'])

    def test_difference(self):
        s1 = Sets(['A', 'B', 'C', 'D'])
        s2 = Sets(['A', 'B', 'C', 'D', 'E'])
        new_set = s1.difference(s2)
        self.assertCountEqual(new_set.set_struct.keys(), [])

        s1 = Sets(['A', 'B', 'C', 'D'])
        s2 = Sets(['A', 'B', 'C', 'D', 'E'])
        new_set = s2.difference(s1)
        self.assertCountEqual(new_set.set_struct.keys(), ['E'])

        s1 = Sets(['A', 'B', 'C'])
        s2 = Sets(['B', 'C', 'D'])
        new_set = s1.difference(s2)
        self.assertCountEqual(new_set.set_struct.keys(), ['A'])

        s1 = Sets(['A', 'B', 'C'])
        s2 = Sets(['D', 'E', 'F'])
        new_set = s1.difference(s2)
        self.assertCountEqual(new_set.set_struct.keys(), ['A', 'B', 'C'])

    def test_is_subSets(self):
        set1 = Sets(['A', 'B', 'C'])
        set2 = Sets(['A', 'B'])
        is_a_subset = set1.is_subset(set2)
        assert is_a_subset == True

        set1 = Sets(['A', 'B', 'C', 'D'])
        set2 = Sets(['A', 'B', 'C', 'D', 'E'])
        is_a_subset = set1.is_subset(set2)
        assert is_a_subset == False

