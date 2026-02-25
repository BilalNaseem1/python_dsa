# 1. two_non_overlapping_pairs
# Find if two non-overlapping pairs exist that sum to the same value.

# two_non_overlapping_pairs([1, 2, 3, 4]) # -> True  (1+4=2+3)
# two_non_overlapping_pairs([1, 1, 1, 1]) # -> True  (1+1=1+1)
# two_non_overlapping_pairs([1, 2, 10])   # -> False


from collections import Counter

def two_non_overlapping_pairs(nums):
    if len(nums) % 2 !=0:
        return False
    
    hmap = Counter(nums)



if __name__ == "__main__":
    print(two_non_overlapping_pairs([1, 2, 10]) )