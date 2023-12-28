# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich, że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)

def bin_na_dec(n):
    n = str(n)
    n = n[::-1]
    suma = 0
    for i in range(len(n)):
        suma += int(n[i]) * 2 ** i
    return suma


def zlozona(n):
    n = bin_na_dec(n)
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


def zad26(A, B):
    ilosc = 0
    n = A + B

    def rek(i, a, b, c):
        nonlocal ilosc
        if i == n - 1:
            if zlozona(c):
                print(c)
                ilosc += 1
                return
            return
        if a > 0:
            rek(i + 1, a - 1, b, c + '1')
        if b > 0:
            rek(i + 1, a, b - 1, c + '0')
        return ilosc
    return rek(0, A-1, B, '1')


print(zad26(2, 3))

