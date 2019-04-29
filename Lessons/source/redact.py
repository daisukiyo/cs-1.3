def redact_lists (array1, array2):
    words_redacted = []  # create empty array to store redacted words
    second = set(array2) # see if a word is banned in constant time O(m)

    for item in array1:  # iterate through each word of the first list O(n)
        if item not in second:  # check if word is in second set O(1)
            words_redacted.append(item) # append banned word to redacted list O(1)
    return words_redacted # return the banned words


print(redact_lists(['A', 'B', 'C'], ['A', 'B']))