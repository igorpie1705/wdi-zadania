# Zadanie 13.
# Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
# Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.


def zad13(n):
    T = [0] * n
    T[0] = n
    i = 0
    while T[0] != 1:
        while T[i] != 1:
            print(T)
            T[i] -= 1
            T[i+1] += 1
            i += 1
        i = 0
    print(T)

zad13(5)

print("NAH IDK")
