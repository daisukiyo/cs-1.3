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
        pass
    
    def test_intersection(self):
        pass

    def test_difference(self):
        pass

    def test_is_subSets(self):
        pass