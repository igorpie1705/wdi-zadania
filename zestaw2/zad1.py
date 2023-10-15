# Zadanie 1.
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie,
# czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

def algorytm(n):
    a, b = 0, 1
    d = 0
    while b <= n:
        if n % b == 0:
            d = n // b
            x, y = a, b
            while y <= d:
                x, y = y, x + y
                if y == d:
                    print("TAK")
                    return 0
        a, b = b, a + b
    print("NIE")


algorytm(178)

