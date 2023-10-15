# Zadanie 7
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie, czy liczba ta jest iloczynem
# dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

def algorytm(n):
    a, b = 0, 1
    while b <= n:
        if a * b == n:
            print("TAK")
            return 0
        a, b = b, a + b
    print("NIE")


algorytm(87841)
