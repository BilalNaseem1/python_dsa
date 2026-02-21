def make_hmap(word):
    hmap = {}
    for i in word:
        if i not in hmap:
            hmap[i] = 0

        hmap[i] += 1
    return hmap

def anagrams(s1, s2):

    return make_hmap(s1) == make_hmap(s2)