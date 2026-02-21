
# Problem:
# Write a function uppercase_strings that takes a list of strings and returns them all in uppercase using map.
# uppercase_strings(["hi","hello"]) -> ["HI","HELLO"]

def uppercase_strings(lst):

    return list(map(lambda x: str(x).upper(), lst))


if __name__ == "__main__":
    print(uppercase_strings(["hi", "hello"]))



# def uppercase_strings(strings):
#     return list(map(str.upper, strings))