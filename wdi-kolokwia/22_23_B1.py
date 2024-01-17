# tab = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]


def sequence(t):
    maxi = 0
    indeks_maxi_p = 0
    indeks_maxi_d = 0
    n = len(t)
    for i in range(1, n):
        dl = 1
        while t[i] > t[i-1] and i < n:
            dl += 1
            i += 1
            if maxi == max(maxi, dl):
                index_maxi_d = i-1
            maxi = max(maxi, dl)
            index_maxi_p = i-1



