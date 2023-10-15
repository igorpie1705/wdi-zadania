# Zadanie 4.
# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze
# nie posiada innych czynników niż 2, 3, 5.
# Jedynka też jest taką liczbą.
# Proszę napisać program, który wylicza ile takich liczb znajduje się w
# przedziale od 1 do N włączni


def algorytm(n):
    count = 0
    for i in range(1, n+1):
        x = i
        while x % 2 == 0:
            x //= 2
        while x % 3 == 0:
            x //= 3
        while x % 5 == 0:
            x //= 5
        if x == 1:
            count += 1
    return count


print(algorytm(10000))
