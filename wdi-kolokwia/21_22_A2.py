from math import log10

tab = [13, 23, 18, 33, 107, 57]


def zamien_na_czworkowy(n):
    liczba = ''
    while n > 0:
        liczba += str(n % 4)
        n //= 4
    return int(liczba[::-1])


def te_same_cyfry(a, b):
    a = zamien_na_czworkowy(a)
    b = zamien_na_czworkowy(b)
    dl_a = int(log10(a))+1
    dl_b = int(log10(b))+1
    tab_a = [0] * 10
    tab_b = [0] * 10
    for i in range(dl_a):
        tab_a[a % 10] += 1
        a //= 10
    for i in range(dl_b):
        tab_b[b % 10] += 1
        b //= 10
    for i in range(10):
        if tab_a[i] > 0 and tab_b[i] == 0 or tab_a[i] == 0 and tab_b[i] > 0:
            return False
    return True


def zadanie(T):
    dl = 0
    N = len(T)
    for i in range(N):
        for j in range(i+1, N):
            if te_same_cyfry(T[i], T[j]):
                dl += 2
                i += 1
    return dl


print(zadanie(tab))
