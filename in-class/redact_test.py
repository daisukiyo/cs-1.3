from redact import redact_lists
import unittest

class RedactTest(unittest.TestCase):

    def word_in_first_not_second(self):
        array1 = ['A', 'B', 'C', 'D', 'E']
        array2 = ['A', 'B', 'C', 'D']
        assert redact_lists(array1, array2) == ['E']

    def empty_arrays(self):
        array1 = []
        array2 = []
        assert redact_lists(array1, array2) == []

    def identical_arrays(self):
        array1 = ['A', 'B', 'C', 'D']
        array2 = ['A', 'B', 'C', 'D']
        assert redact_lists(array1, array2) == ['']

if __name__ == '__main__':
    unittest.main()
# return [item for item in first if item not in second]