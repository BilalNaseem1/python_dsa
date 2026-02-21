# Write a function, pairs, that takes in a list as an argument. 
# The function should return a list containing all unique pairs of elements.
# You may return the pairs in any order and the order of elements within a single pair does not matter.
# You can assume that the input list contains unique elements.

FUNCTION = "pairs"

TESTS = [
    # basic small case
    (
        ([1, 2, 3],),
        [[1, 2], [1, 3], [2, 3]]
    ),

    # two elements
    (
        (["a", "b"],),
        [["a", "b"]]
    ),

    # four elements
    (
        ([4, 5, 6, 7],),
        [
            [4, 5],
            [4, 6],
            [4, 7],
            [5, 6],
            [5, 7],
            [6, 7],
        ]
    ),

    # empty list
    (
        ([],),
        []
    ),

    # single element
    (
        ([42],),
        []
    ),
]
