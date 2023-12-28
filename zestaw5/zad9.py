tab = [1, 10, 15]


def zad9(T, masa):
    n = len(T)

    def rek(i, w, tablica):
        if i == n:
            if w == masa:
                print(tablica)
                return True
            return False
        return rek(i + 1, w, tablica) or rek(i + 1, w + T[i], tablica + [T[i]]) or rek(i + 1, w - T[i], tablica + [T[i]])

    return rek(0, 0, [])


print(zad9(tab, 6))
