# Processing
def bitcoin(current_price):
    benefits = round((0.00456517 * (current_price - 8762)) * 100) / 100     # Forme factorisée de round((current_price * 0.00456517 - 8762 * 0.00456517) * 100) / 100
    if benefits >= 0:
        return "Gain de " + str(benefits) + " euros"
    else:
        return "Perte de " + str(abs(benefits)) + " euros"


# Unit Tests API Input
# print(bitcoin(lines[0]))

# Tests
print(bitcoin(10200))   # Must return "Gain de 6.56 euros"
print(bitcoin(8762))    # Must return "Gain de 0.0 euros"
print(bitcoin(7900))    # Must return "Perte de 3.94 euros"
print(bitcoin(float(input("::"))))
