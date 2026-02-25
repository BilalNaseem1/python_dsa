# exclusive items
# Write a function, exclusive_items, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in either list but not both lists.

# You may assume that each input list does not contain duplicate elements.


# exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]
# exclusive_items([2,4,6], [4,2]) # -> [6]
# exclusive_items([4,2,1], [1,2,4,6]) # -> [6]
# exclusive_items([0,1,2], [10,11]) # -> [0,1,2,10,11]
# a = [ i for i in range(0, 50000) ]
# b = [ i for i in range(0, 50000) ]
# exclusive_items(a, b) # -> [ ]


def exclusive_items(a, b):
    output = []

    set_a = set(a)
    set_b = set(b)

    for i in set_a:
        if i not in set_b:
            output.append(i)

    for j in set_b:
        if j not in set_a:
            output.append(j)


    return output
