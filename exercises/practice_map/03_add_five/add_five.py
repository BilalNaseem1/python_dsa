# Write a function add_five that takes a list of numbers and returns a list where 5 is added to each element using map.
# add_five([1,2,3]) -> [6,7,8]

def add_five(nums):
    return list(map(lambda x: x+5, nums))


if __name__ == "__main__":
    print(add_five([1,2,3]))