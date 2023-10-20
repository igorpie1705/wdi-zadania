# Zadanie 15.
# Proszę napisać program znajdujący wszystkie liczby N-cyfrowe,
# dla których suma N-tych potęg cyfr liczby jest równa tej liczbie,
# np. 153 = 1^3 + 5^3 + 3^3.

def algorytm(n):
    for i in range(10 ** (n - 1), 10 ** n):
        if sprawdz(n, i):
            print(i)


def sprawdz(n, m):
    x = 0
    i = 1
    while x <= m:
        if i ** n > m:
            break
        x = i ** n
        i += 1
    while i > 0:
        if x + i ** n <= m:
            x += (i ** n)
            i -= 1
        else:
            i -= 1
    if x == m:
        return True
    else:
        return False


algorytm(3)
