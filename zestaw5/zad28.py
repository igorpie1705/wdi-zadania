# Zadanie 28. Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
# która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
# podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
# [5, 7, 15] → f alse, podział nie istnieje.

T = [5, 1, 2, 3, 5, 7, 15]


def licz(n):
    cnt = 0
    for i in n:
        while i > 0:
            if i % 2 == 1:
                cnt += 1
            i //= 2
    return cnt


def zad28(T):
    n = len(T)

    def rek(i, a, b, c):
        if i == n:
            if licz(a) == licz(b) == licz(c):
                print(a, b, c)
                return True
            return False

        if rek(i + 1, a + [T[i]], b, c) or rek(i + 1, a, b + [T[i]], c) or rek(i + 1, a, b, c + [T[i]]):
            return True
        return False

    return rek(0, [], [], [])


print(zad28(T))
