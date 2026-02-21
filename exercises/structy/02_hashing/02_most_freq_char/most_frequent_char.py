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
