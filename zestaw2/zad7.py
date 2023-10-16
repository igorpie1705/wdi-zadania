# Zadanie 7.
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie, czy liczba ta jest wielokrotnością
# dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

def algorytm(x):
    a, n = 0, 1
    while a <= x:
        a = n * n + n + 1
        if x % a == 0:
            print("TAK")
            return
        n += 1
    print("NIE")


algorytm(344)
