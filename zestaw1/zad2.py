# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

def nowy_fibonacci():
    min_suma, x, y = 2023, 0, 0
    for n in range(1, 2023):
        for m in range(1, 2023):
            a, b = m, n
            while b <= 2023:
                if b == 2023:
                    if n + m <= min_suma:
                        min_suma = n + m
                        x, y = n, m
                a, b = b, a + b
    print(x, y)

nowy_fibonacci()
