# Processing
def scrabble(word):
    wordPoints = 0
    word = word.lower()

    for letter in word:
        if letter in ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'u', 'l']:
            wordPoints += 1
        elif letter in ['d', 'm', 'g']:
            wordPoints += 2
        elif letter in ['b', 'c', 'p']:
            wordPoints += 3
        elif letter in ['f', 'h', 'v']:
            wordPoints += 4
        elif letter in ['j', 'q']:
            wordPoints += 8
        elif letter in ['k', 'w', 'x', 'y', 'z']:
            wordPoints += 10
        else:
            return -1

    return wordPoints


# Unit Tests API Input
# print(scrabble(lines[0]))

# Tests
print(scrabble("chameau"))  # Must return 13
print(scrabble("scorpion"))  # Must return 12
print(scrabble("épée"))  # Must return -1
print(scrabble("epee"))  # Must return 6
