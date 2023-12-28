
from math import sqrt

def dzielniki(n):
    i = 2
    dzieln = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            dzieln.append(i)
            while n % i == 0:
                n //= i
    if n != 1:
        dzieln.append(n)
    return dzieln


def zad31(num):
    divs = dzielniki(num)
    n = len(divs)
    Sum = 0

    def rek(prod, i):
        nonlocal Sum
        if i == n:
            Sum += prod
        else:
            rek(prod * divs[i], i + 1)
            rek(prod, i + 1)
    rek(1, 0)

    return Sum - 1


print(zad31(60))
