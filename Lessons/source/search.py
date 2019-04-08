#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    #  check if index is out of bound
    if index >= len(array):
        return None
    #  if the value at a specific index of array is equivalent to the target value...
    if array[index] == item:
        #  return the first index of item in array
        return index

    #  recursively call the function while incrementing the index value
    return linear_search_recursive(array, item, index + 1)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    #  initialize the lower and upper bound for the array
    left = 0  # lower
    right = len(array) - 1  # upper

    while left <= right:

        #  find the rounded middle point via floor division
        mid = (left + right) // 2

        #  if the value at a specific index of array is equivalent to the target value...
        if item == array[mid]:
            #  return the first index of item in array
            return(mid)
        #  if the targeted item is less than the middle point...
        elif item < array[mid]:
            #  shift the upper bound to the middle point
            right = mid - 1
        #  the targeted item is greater than the middle point
        else:
            #  shift the lower bound to the middle point
            left = mid + 1

    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    #  initialize the lower and upper bound for the array
    if left == None: 
        left = 0
    if right == None:
        right = len(array) -1
    
    #  check edge case where array is non-existent (lower bound cannot be greater than upper bound)
    if left > right:
        return None
    else:
        #  find the rounded middle point via floor division
        mid = (left + right) // 2
        #  if the value at a specific index of array is equivalent to the target value...
        if item == array[mid]:
            #  return the first index of item in array
            return(mid)
        #  if the targeted item is less than the middle point...
        elif item < array[mid]:
            #  recursively calls itself with a new upper bound
            return binary_search_recursive(array, item, left, mid-1)
        #  the targeted item is greater than the middle point
        else:
            #  recursively calls itself with a new lower bound
            return binary_search_recursive(array, item, mid+1, right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests