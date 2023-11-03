# Zadanie 16.
# Mamy zdefiniowaną n-elementową tablicę liczb całkowitych.
# Proszę napisać funkcję zwracającą wartość typu bool oznaczającą,
# czy w tablicy istnieje dokładnie jeden element
# najmniejszy i dokładnie jeden element największy
# (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej wartości).

from random import randint


def algorytm(n):
    tab = []
    for i in range(n):
        tab.append(randint(1, 10))
    print(tab)
    mini = 11
    maxi = 0
    l_mini = 0
    l_maxi = 0
    tylko_jeden = False
    for i in range(n):
        if tab[i] < mini:
            mini = tab[i]
        if tab[i] > maxi:
            maxi = tab[i]
    for i in range(n):
        if tab[i] == mini:
            l_mini += 1
        if tab[i] == maxi:
            l_maxi += 1
    if l_mini + l_maxi > 2:
        return False
    return True


print(algorytm(10))

