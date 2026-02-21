FUNCTION = "anagrams"

TESTS = [
    (("restful", "fluster"), True),
    (("cats", "tocs"), False),
    (("monkeyswrite", "newyorktimes"), True),
    (("paper", "reapa"), False),
    (("pp", "oo"), False),
    (("po", "popp"), False),
    (("abbc", "aabc"), False),
    (("night", "thing"), True),
    (("taxi", "tax"), False),
    (("elbow", "below"), True),

    # additional edge cases
    (("", ""), True),                # empty strings
    (("a", "a"), True),              # single character match
    (("a", "b"), False),             # single character mismatch
]
