# Zadanie 1.
# Napisać funkcję zamieniającą i wypisującą
# liczbę naturalną na system o podstawie 2-16.

def zamien(n, p):
    liczba = ''
    while n > 0:
        dodaj = n % p
        n //= p
        if dodaj > 10:
            dodaj = chr(ord('A') + dodaj - 10)
            liczba += str(dodaj)
        else:
            liczba += str(dodaj)
    return liczba[::-1]


print(zamien(234, 16))

