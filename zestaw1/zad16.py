# Zadanie 16
# Dany jest ciąg określony wzorem:
# An+1 = (An mod2)∗(3∗An +1)+(1−An mod2)∗An/2
# Startując z dowolnej liczby naturalnej > 1
# ciąg ten osiąga wartość 1. Proszę napisać program,
# który znajdzie wyraz początkowy z przedziału 2-10000
# dla którego wartość 1 jest osiągalna po największej liczbie kroków


def algorytm():
    EPS = 1e-6
    max_count = 0
    pom = 0
    for i in range(2, 10000+1):
        count = 1
        a = i
        while abs(a-1) < EPS:
            a = (a % 2) * (3 * a + 1) + (1 - a % 2) * a / 2
            count += 1
            if count > max_count:
                pom = i
    return pom


print(algorytm())
