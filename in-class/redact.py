def redact_lists (array1, array2):
    words_redacted = []
    second = set(array2)

    for item in array1:
        if item not in second:
            words_redacted.append(item)
    return(words_redacted)


print(redact_lists(['A', 'B', 'C'], ['A', 'B']))