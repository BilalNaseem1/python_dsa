# all unique

# Write a function, all_unique, that takes in a list. The function should return a boolean indicating whether or not the list contains unique items.
# all_unique(["q", "r", "s", "a"]) # -> True
# all_unique(["q", "r", "s", "a", "r", "z"]) # -> False
# all_unique(["red", "blue", "yellow", "green", "orange"]) # -> True
# all_unique(["cat", "cat", "dog"]) # -> False
# all_unique(["a", "u", "t", "u", "m", "n"]) # -> False


def all_unique(lst):
    return len(set(lst)) == len(lst)



if __name__ == "__main__":
    print(all_unique(["q", "r", "s", "a"]))