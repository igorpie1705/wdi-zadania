# Zadanie 4. Proszę napisać program obliczający pierwiastek
# całkowitoliczbowy z liczby naturalnej korzystając z
# zależności 1 + 3 + 5 + ... = n2.

def algorytm(n):
    i = 1
    s = 0
    w = 0
    while s < n:
        s += i
        i += 2
        w += 1
    if s == n:
        print(w)
    else:
        print("BRAK PIERWIASTKA CAŁKOWITOLICZBOWEGO")


algorytm(625)

