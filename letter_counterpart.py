losedBracketWord(word):
    if len(word) == 0:
        return True
    if len(word) % 2 != 0:
        return False
    x = 'abcdefghijklmnopqrstuvwxyz'
    word = word.lower()
    result = False
    for i in range(len(word)/2):
        index_x = x.index(word[i])
        if word[(i-i-i) + -1] == x[(26-index_x)-1]:
            result = True
        else:
            return False
    return result

