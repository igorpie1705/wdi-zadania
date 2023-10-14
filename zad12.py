# Zadanie 12
# Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(nwd(60, 48))

