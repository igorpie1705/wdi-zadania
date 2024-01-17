tab = [[5, 4, 1, 6, 7],
       [4, 2, 1, 3, 9],
       [7, 6, 1, 8, 2],
       [9, 1, 9, 2, 92],
       [5, 2, 14, 14, 1]]


def nalezy(n):
    a, b = 1, 2
    if n == a or n == b:
        return True
    for i in range(n + 1):
        a, b = b, a + b - 1
        if b == n:
            return True
    return False


def seq(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            x = 2
            cnt = 0
            while i + x < n and j + x < n and T[i + x][j + x] == T[i + x - 2][j + x - 2] + T[i + x - 1][
                j + x - 1] - 1 and nalezy(T[i + x][j + x]):
                cnt += 1
                x += 1
            if cnt > 0:
                return cnt + 2


print(seq(tab))
