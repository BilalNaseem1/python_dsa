FUNCTION = "intersection_with_dupes"

TESTS = [
    (
        (["a", "b", "c", "b"], ["x", "y", "b", "b"]),
        ["b", "b"]
    ),
    (
        (["q", "b", "m", "s", "s", "s"], ["s", "m", "s"]),
        ["m", "s", "s"]
    ),
    (
        (["p", "r", "r", "r"], ["r"]),
        ["r"]
    ),
    (
        (["r"], ["p", "r", "r", "r"]),
        ["r"]
    ),
    (
        (["t", "v", "u"], ["g", "e", "d", "f"]),
        []
    ),
    (
        (["a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a"]),
        ["a", "a", "a", "a"]
    ),
    (
        (
            [i for i in range(150000)],
            [i for i in range(150000)]
        ),
        [i for i in range(150000)]
    ),
]