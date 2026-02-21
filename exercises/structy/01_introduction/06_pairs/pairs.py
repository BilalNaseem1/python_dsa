# Write a function, pairs, that takes in a list as an argument. 
# The function should return a list containing all unique pairs of elements.
# You may return the pairs in any order and the order of elements within a single pair does not matter.
# You can assume that the input list contains unique elements.



def pairs(lst):

    output = []

    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            pair = [lst[i], lst[j]]
            output.append(pair)
    return output




