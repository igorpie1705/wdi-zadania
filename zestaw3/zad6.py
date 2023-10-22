# Zadanie 6.
# Napisać program wypełniający N-elementową tablicę
# t liczbami naturalnymi 1-1000 i sprawdzający, czy każdy element
# tablicy zawiera co najmniej jedną cyfrę nieparzystą.


from random import randint


def algorytm(n):
    tab = []
    for i in range(n):
        tab.append(randint(1, 1000))
    for i in tab:
        x = i
        nieparzysta = False
        while x > 0:
            a = x % 10
            x //= 10
            if a % 2 == 1:
                nieparzysta = True
                break
        if nieparzysta is False:
            print("NIE")
            print(tab)
            return
    print("TAK")
    print(tab)


algorytm(3)
