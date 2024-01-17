# Zadanie 17. Dane są dwie liczby naturalne, z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić
# wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb wejściowych musi być
# zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523, 75123, 17253 itd. Proszę napisać
# funkcję, która wyznaczy ile liczb pierwszych można zbudować z dwóch zadanych liczb.

from math import sqrt


def czy_pierwsza(n):
    n = int(n)
    i = 2
    if n < 2:
        return False
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def zad17(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    cnt = 0
    n = len(num1) + len(num2)

    def rek(i, a, b, c):
        print(c)
        nonlocal cnt
        if i == n:
            print(c)
            if czy_pierwsza(c):
                cnt += 1
            return

        if len(a) > 0:
            rek(i + 1, a[1:], b, c + a[0])
        if len(b) > 0:
            rek(i + 1, a, b[1:], c + b[0])
        return cnt

    return rek(0, num1, num2, '')


print(zad17(123, 75))
