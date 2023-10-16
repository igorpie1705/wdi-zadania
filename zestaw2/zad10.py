# Zadanie 10.
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie, czy liczba ta jest wielokrotnością
# dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest równy 2.

def algorytm(x):
    a = 2
    while a <= x:
        a = 3 * a + 1
        if x % a == 0:
            print("TAK")
            return
    print("NIE")


algorytm(594)
