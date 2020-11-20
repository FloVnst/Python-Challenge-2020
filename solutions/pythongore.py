# Processing
def pythongore(cotes: list):
    hypothenuse = max(cotes)
    autresCotes = cotes
    autresCotes.remove(hypothenuse)
    return hypothenuse**2 == autresCotes[0]**2 + autresCotes[1]**2


# Unit Tests API Input
# print(pythongore([lines[0], lines[1], lines[2]]))


# Tests
print(pythongore([3, 4, 5]))            # Must return True
print(pythongore([88, 105, 137]))       # Must return True
print(pythongore([696, 697, 985]))      # Must return True
print(pythongore([646, 697, 915]))      # Must return False
print(pythongore([38, 22, 55]))         # Must return False
print(pythongore([158, 38, 450]))       # Must return False
print(pythongore([6, 7, 8]))            # Must return False
print(pythongore([6, 8, 10]))            # Must return Trur
