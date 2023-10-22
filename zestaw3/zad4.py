# Zadanie 4.
# Napisać program obliczający i wypisujący stałą e
# z rozwinięcia w szereg e = 1/0! + 1/1! + 1/2! + 1/3! + ...
# z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

def algorytm(n):
    e = 1
    eps = 0.1 ** n
    tab = [0, 1]
    i = 1
    while abs(tab[0] - tab[1]) > eps:
        silnia = 1
        for j in range(1, i+1):
            silnia *= j
        tab[0] = e
        e += 1/silnia
        tab[1] = e
        print(e)
        i += 1


algorytm(78)




