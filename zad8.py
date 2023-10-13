# Zadanie 8
# Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if pierwsza(797):
    print("TAK")
