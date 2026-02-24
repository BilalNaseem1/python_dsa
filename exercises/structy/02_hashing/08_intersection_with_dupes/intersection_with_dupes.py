# intersection_with_dupes(
#   ["a", "b", "c", "b"], 
#   ["x", "y", "b", "b"]
# ) # -> ["b", "b"]


# intersection_with_dupes(
#   ["q", "b", "m", "s", "s", "s"], 
#   ["s", "m", "s"]
# ) # -> ["m", "s", "s"]

# intersection_with_dupes(
#   ["p", "r", "r", "r"], 
#   ["r"]
# ) # -> ["r"]

# intersection_with_dupes(
#   ["r"], 
#   ["p", "r", "r", "r"]
# ) # -> ["r"]

# intersection_with_dupes(
#   ["t", "v", "u"], 
#   ["g", "e", "d", "f"]
# ) # -> [ ]


# intersection_with_dupes(
#   ["a", "a", "a", "a", "a", "a",], 
#   ["a", "a", "a", "a"]
# ) # -> ["a", "a", "a", "a"]

# a = []
# b = [] 
# for i in range(0, 150000):
#   a.append(i)
#   b.append(i)

# intersection_with_dupes(a, b) # -> [0, 1, 2, ..., 149999]

from collections import Counter

# def make_counter(lst):
#     hmap = {}

#     for i in lst:
#         if i not in hmap:
#             hmap[i] = 0

#         hmap[i] += 1

#     return hmap


def intersection_with_dupes(a, b):
    hmap_a = Counter(a)
    hmap_b = Counter(b)
    output = []
    
    for i in hmap_a:
        for j in range(0, min(hmap_a[i], hmap_b[i])):
            output.append(i)

    return output

if __name__ == "__main__":
    print(intersection_with_dupes(["q", "b", "m", "s", "s", "s"], ["s", "m", "s"])) # -> ["m", "s", "s"]