# Zadanie 19. Proszę napisać program wyznaczający
# wartość liczby e korzystając z zależności: e = 1/0! +1/1!+1/2!+1/3!+...


def algorytm():
    e = 0
    for i in range(100):
        silnia = 1
        for j in range(1, i+1):
            silnia *= j
        e += 1/silnia
    return e


print(algorytm())
