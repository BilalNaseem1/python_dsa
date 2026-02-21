FUNCTION = "most_frequent_char"

TESTS = [
    (("bookeeper",), "e"),
    (("david",), "d"),
    (("abby",), "b"),
    (("mississippi",), "i"),
    (("potato",), "o"),
    (("eleventennine",), "e"),
    (("riverbed",), "r"),

    # additional edge cases
    (("a",), "a"),           # single character
    (("aaabbb",), "a"),      # tie: first max character
    (("",), None),            # empty string, could return None
]
