from math import sqrt, log10


def roznocyfrowa(n):
    t = [0] * 10
    dl = int(log10(n))+1
    for i in range(dl):
        t[n % 10] += 1
        n //= 10
    for i in t:
        if i > 1:
            return False
    return True


def czy_pierwsza_plus(n):
    if not roznocyfrowa(n):
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def obcinaj(l):
    l = str(l)
    n = len(l)
    maxi = 0
    M = 0
    N = 0
    for N in range(n):
        M = 0
        while M + N < n - 1:
            obciete = l[M:n - N]
            if czy_pierwsza_plus(int(obciete)):
                maxi = max(int(obciete), maxi)
            M += 1
    return maxi


print(obcinaj(12027449910339213516))
