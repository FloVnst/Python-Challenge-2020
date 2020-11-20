# Processing
def scrabble(word):
    wordPoints = 0
    lettersPoints = {
        1: ['e', 'a', 'i', 'n', 'o', 'r', 's', 't', 'u', 'l'],
        2: ['d', 'm', 'g'],
        3: ['b', 'c', 'p'],
        4: ['f', 'h', 'v'],
        8: ['j', 'q'],
        10: ['k', 'w', 'x', 'y', 'z']
    }
    word = word.lower()

    for letter in word:
        is_valid = False
        for points, letters in lettersPoints.items():
            if letter in letters:
                is_valid = True
                wordPoints += points
                break
        if not is_valid:
            # error = "\'" + letter + "\' is not a valid character."
            raise Exception("-1")

    return wordPoints


# Unit Tests API Input
# print(scrabble(lines[0]))

# Tests
print(scrabble("chameau"))      # Must return 13
print(scrabble("scorpion"))     # Must return 12
print(scrabble("oracle"))       # Must return 12
print(scrabble("paladin"))      # Must return 12
print(scrabble("pingouin"))     # Must return 11
print(scrabble("Whiskey"))      # Must return 37
