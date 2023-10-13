# Zadanie 10
# Proszę napisać program wyszukujący liczby doskonałe mniejsze od miliona


def doskonale():
    for n in range(1, 10000):
        sum1 = 0
        for i in range(1, n):
            if n % i == 0:
                sum1 = sum1 + i
        if sum1 == n:
            print(n)


doskonale()
