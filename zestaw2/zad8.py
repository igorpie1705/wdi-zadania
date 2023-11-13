# Zadanie 8.
# Pewnych liczb nie można przedstawić jako sumy
# elementów spójnych fragmentów ciągu Fibo- nacciego,
# np. 9, 14, 15, 17, 22.
# Proszę napisać program, który wczytuje liczbę naturalną n,
# wylicza i wypisuje następną taką liczbę większą od n.
# Można założyć, że 0 < n < 1000.

# 0 1 1 2 3 5 8


def da_sie_fib(n):
    a, b = 0, 1
    suma = 1
    while b < n:
        a, b = b, a + b
        suma += b
        if n == suma:
            return True
        else:
            suma2 = suma
            c, d = 0, 1
            while suma2 > 0:
                c, d = d, c + d
                suma2 -= c
                if n == suma2:
                    return True
    return False


def algorytm(n):
    i = n + 1
    while True:
        if da_sie_fib(i) is False:
            print(i)
            return
        else:
            i += 1

algorytm(44)
print("ez dziala")
