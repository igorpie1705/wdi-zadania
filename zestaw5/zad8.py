T = [1, 10, 15]


def zad8(T, masa):
    n = len(T)

    def rek(i, w):
        if i == n:
            if w == masa:
                return True
            return False

        return rek(i+1, w) or rek(i+1, w + T[i]) or rek(i+1, w - T[i])

    return rek(0, 0)


print(zad8(T, 13))


