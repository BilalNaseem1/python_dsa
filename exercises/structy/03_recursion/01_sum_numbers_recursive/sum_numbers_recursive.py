# sum numbers recursive

# Watch the Approach video first!

# Write a function sum_numbers_recursive that takes in an array of numbers and returns
# the sum of all the numbers in the array. All elements will be integers. Solve this recursively.

# sum_numbers_recursive([5, 2, 9, 10]); # -> 26
# sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1]); # -> 1
# sum_numbers_recursive([]); # -> 0
# sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1]); # -> 1001
# sum_numbers_recursive([700, 70, 7]); # -> 777
# sum_numbers_recursive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]); # -> -55
# sum_numbers_recursive([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]); # -> 0
# sum_numbers_recursive([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]); # -> 137174205


def sum_numbers_recursive(nums):

    if len(nums) == 0:
        return 0

    return nums[0] + sum_numbers_recursive(nums[1:])