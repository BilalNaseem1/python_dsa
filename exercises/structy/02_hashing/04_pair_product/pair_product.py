

# Write a function, pair_product, that takes in a list and a target product as arguments. 
# The function should return a tuple containing a pair of indices whose elements multiply to the given target. 
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.


# pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
# pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
# pair_product([4, 7, 9, 2, 5, 1], 5) # -> (4, 5)
# pair_product([4, 7, 9, 2, 5, 1], 35) # -> (1, 4)
# pair_product([3, 2, 5, 4, 1], 10) # -> (1, 2)
# pair_product([4, 6, 8, 2], 16) # -> (2, 3)
# numbers = [ i for i in range(1, 6001) ]
# pair_product(numbers, 35994000) # -> (5998, 5999) 


def make_hmap(nums):
    hmap = {}

    for index, val in enumerate(nums):
        hmap[val] = index

    return hmap


def pair_product(nums, target):
    
    hmap = make_hmap(nums)

    for index, val in enumerate(hmap):
        other = target / val

        if other in hmap and index != hmap[other]:
            return index, hmap[other]




if __name__ == "__main__":
    print(pair_product([3, 2, 5, 4, 1], 8))