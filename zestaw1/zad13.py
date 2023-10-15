# Zadanie 13
# Proszę napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.

def nww(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return a * b // x


print(nww(523432, 195324))
