
# anagrams

# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams.
# Anagrams are strings that contain the same characters, but in any order.
# anagrams('restful', 'fluster') # -> True
# anagrams('cats', 'tocs') # -> False
# anagrams('tax', 'taxi') # -> False
# anagrams('pp', 'oo') # -> false
# anagrams('night', 'thing') # -> True



def make_hmap(word):
    hmap = {}
    for i in word:
        if i not in hmap:
            hmap[i] = 0

        hmap[i] += 1
    return hmap

def anagrams(s1, s2):

    return make_hmap(s1) == make_hmap(s2)