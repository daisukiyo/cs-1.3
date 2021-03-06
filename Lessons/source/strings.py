#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    O(n) runtime"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    
    pattern_index = find_index(text, pattern)

    if pattern_index != None:
        return True
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."" "
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    O(n) where n is the index where the last pattern is in the string"""

    # return "0" when no pattern is found
    if pattern == "":
        return 0

    # declare an index for botth the pattern in text and itself    
    index = 0
    sub_index = 0

    # initialize the starting point
    start = 0

    while index <= len(text) - 1:
        # compare first letter the text to the first of the pattern
        if text[index] == pattern[sub_index]:
            index += 1
            sub_index += 1

            if sub_index == len(pattern):
                return start
        else:
            start += 1
            index = start
            sub_index = 0

    return None

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    O(n) where n is the number of letters in the text"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    if pattern == "":
        return list(range(len(text)))
    
    # using find index to obtain the index of the first occurance
    index = find_index(text, pattern)

    # create a list of all the indicies
    start_indexes = []

    if index != None:
        # append each indice to the list
        start_indexes.append(index)

        # initialize reference points
        index = index + 1
        start = index
        sub_index = 0

        while index <= len(text) - 1:
            # using the reference poitns initialized above
            # traverse the chunk of text over 1 index at a time
            # checking everytime a pattern potentially matches
            if text[index] == pattern[sub_index]:
                index += 1
                sub_index += 1

                # if you reach the end of the pattern, its a match
                if sub_index == len(pattern):
                    start_indexes.append(start)
                    # restart search pattern
                    sub_index = 0
                    start += 1
                    index = start
            else:
                sub_index = 0
                start += 1
                index = start
        return start_indexes
    return start_indexes


        


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    print(contains('abc', 'a'))
