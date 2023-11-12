# Zadanie 6
# Proszę napisać program rozwiązujący równanie x^x = 2020 metodą bisekcji.

def f(x):
    return pow(x,x) - 2020


def algorytm():
    a = -100
    b = 100
    EPS = 0.0001
    while abs(a-b) >= EPS:
        srodek = (a+b)/2
        if f(srodek) == 0.0:
            return srodek
        elif f(a) * f(srodek) < 0:
            b = srodek
        elif f(srodek) * f(b) < 0:
            a = srodek
    return (a + b) / 2


print(algorytm())

print(pow(4.8316, 4.8316))

