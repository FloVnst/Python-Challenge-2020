# Processing
def luhn(cardNumber):
    if len(cardNumber) == 16:
        checksum = 0
        i = 0
        for digit in cardNumber:
            digit = int(digit)
            if i % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
            i += 1
        return checksum % 10 == 0
    else:
        return False


# Unit Tests API Input
# print(luhn(lines[0]))


# Tests
print(luhn("6703111122223334"))  # Must return True
print(luhn("6703111122223338"))  # Must return False
print(luhn("6703111122223331"))  # Must return False
print(luhn("6703111122223336"))  # Must return False
print(luhn("6703111122223333"))  # Must return False
print(luhn("6803111122223333"))  # Must return True
print(luhn("6776111854223134"))  # Must return False
print(luhn("6103111122423339"))  # Must return False
print(luhn("6803511122223334"))  # Must return True
print(luhn("7803511122223332"))  # Must return True
print(luhn("7803511122223336"))  # Must return False
print(luhn("7803511132223330"))  # Must return True
print(luhn("7803511132223331"))  # Must return False
print(luhn("7803511132223333"))  # Must return False
print(luhn("7803511132223337"))  # Must return False
print(luhn("7809511132223334"))  # Must return True
print(luhn("7809511132223332"))  # Must return False
print(luhn("7809511132223331"))  # Must return False
print(luhn("7809511132223333"))  # Must return False
print(luhn("7809511132223336"))  # Must return False
