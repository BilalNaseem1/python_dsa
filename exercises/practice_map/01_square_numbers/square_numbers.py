
# Problem:
# Write a function square_numbers that takes a list of numbers and returns a list of their squares using map.
# square_numbers([1,2,3,4]) -> [1,4,9,16]

def square_numbers(nums):
    return list(map(lambda x: x**2, nums))


if __name__ == "__main__":
    print(square_numbers([1,2,3,4]))