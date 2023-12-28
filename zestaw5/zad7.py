T = [1, 5, 8, 12, 25]


def zad7(T, masa):
    n = len(T)

    def rek(i, w):
        if i == n:
            if w == masa:
                return True
            return False

        return rek(i+1, w) or rek(i+1, w + T[i])

    return rek(0, 0)


print(zad7(T, 12))


