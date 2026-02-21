def longest_word(sentence):

    words = sentence.split(" ")
    max_len = float('-inf')
    max_word = ""

    for i in words:
        if len(i) >= max_len:
            max_word = i
            max_len = len(i)

    return max_word


# longest_word("hello my")