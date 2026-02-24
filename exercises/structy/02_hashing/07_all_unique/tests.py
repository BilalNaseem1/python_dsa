FUNCTION = "all_unique"

TESTS = [
    ((["q", "r", "s", "a"],), True),
    ((["q", "r", "s", "a", "r", "z"],), False),
    ((["red", "blue", "yellow", "green", "orange"],), True),
    ((["cat", "cat", "dog"],), False),
    ((["a", "u", "t", "u", "m", "n"],), False),
]