# Zadanie 18.
# Mamy dane dwa ciągi A, B o następujących zależnościach:
# A:a0 =0,a1 =1,an =an−1−bn−1∗an−2
# B: b0 = 2, bn = bn−1 + 2 ∗ an−1
# Proszę napisać program, który czyta liczby typu int
# ze standardowego wejścia i tak długo jak liczby te są kolejnymi
# wyrazami ciągu An (tj. a0,a1,a2, ...) wypisuje na standardowe wyjście
# wyrazy drugiego ciągu Bn (tj. b0, b1, b2, ...).


def b(n):
    if n == 0:
        return 2
    return b(n-1) + 2 * a(n-1)


def a(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return a(n-1) - b(n-1) * a(n-2)


for i in range(10):
    print(i, a(i), b(i))
