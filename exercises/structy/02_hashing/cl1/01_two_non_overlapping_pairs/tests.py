FUNCTION = "two_non_overlapping_pairs"

TESTS = [
    (
        ([1, 2, 3, 4],),
        True
    ),
    (
        ([1, 1, 1, 1],),
        True
    ),
    (
        ([1, 2, 10],),
        False
    ),
    (
        ([1, 5, 3, 2, 4],),
        True
    ),
    (
        ([1],),
        False
    ),
    (
        ([],),
        False
    ),
    (
        ([3, 3, 3, 3],),
        True
    ),
]