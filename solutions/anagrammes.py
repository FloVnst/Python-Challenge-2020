# Processing
def anagrams(word1, word2):
    return word1 != word2 and sorted(word1.lower()) == sorted(word2.lower())


# Unit Tests API Input
# print(anagrams(lines[0], lines[1]))

# Tests
print(anagrams("migraine", "imaginer"))  # Must return True
print(anagrams("Pirate", "partie"))  # Must return True
print(anagrams("hello", "hola"))  # Must return False
print(anagrams("hello", "hello"))  # Must return False
