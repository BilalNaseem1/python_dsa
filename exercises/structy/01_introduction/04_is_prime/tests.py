FUNCTION = "is_prime"

TESTS = [
    ( [ 2], True  ),
    ( [ 3], True  ),
    ( [ 4], False ),
    ( [ 5], True  ),
    ( [ 6], False ),
    ( [ 7], True  ),
    ( [ 8], False ),
    ( [ 25], False ),
    ( [31], True ),
    ( [2017], True ),
    ([2048], False),
    ([1], False),
    ([713], False)
]
