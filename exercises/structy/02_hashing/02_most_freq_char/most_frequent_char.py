# most frequent char

# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. 
# If there are ties, return the character that appears earlier in the string.
# You can assume that the input string is non-empty.

# most_frequent_char('bookeeper') # -> 'e'
# most_frequent_char('mississippi') # -> 'i'


def make_hmap(word):
    hmap = {}

    for i in word:
        if i not in hmap:
            hmap[i] =0

        hmap[i] +=1

    return hmap

def most_frequent_char(s):
    hmap_s = make_hmap(s)

    max_char = ""
    max_len = float('-inf')

    if s == '':
        return None

    for k, v in hmap_s.items():
        if v > max_len:
            max_len = v
            max_char = k

    return max_char
