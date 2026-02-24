# Write a function, pair_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a pair of indices whose elements sum to the given target.
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.


# pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)
# pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)
# pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
# pair_sum([1, 6, 7, 2], 13) # -> (1, 2)

def make_hmap(nums):
    hmap = {}

    for index, val in enumerate(nums):
        hmap[val] = index

    return hmap

def pair_sum(nums, target):

    hmap = make_hmap(nums)

    for index, val in enumerate(nums):
        other = target - val

        if other in hmap and index != hmap[other]:
            return index, hmap[other]




if __name__ == "__main__":
    print(pair_sum([3, 2, 5, 4, 1], 8))
        

