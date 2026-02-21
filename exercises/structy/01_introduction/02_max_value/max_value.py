def max_value(nums):
    max_val = float('-inf')

    for i in nums:
        if i> max_val:
            max_val = i

    return max_val
