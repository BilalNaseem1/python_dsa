# Problem:
# Write a function to_strings that converts a list of numbers into a list of strings using map.
# to_strings([1,2,3]) -> ["1","2","3"]


def to_strings(nums):
    return list(map(lambda x: str(x), nums))



if __name__ == "__main__":
    print(to_strings([1,2,3]))