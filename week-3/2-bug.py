def path(p, n, m, way):
    if n == 0 and m == 0:
        print(''.join(way))
        return
    if p[n][m] == 1:
        way.insert(0, 'r')
        path(p, n, m-1, way)
    elif p[n][m] == 2:
        way.insert(0, 'd')
        path(p, n-1, m, way)
    else:
        print(n, m)


def bug(a):
    n = len(a)
    m = len(a[0])
    p = [None] * n
    for i in range(n):
        p[i] = [0] * m
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                a[i][j] += a[i][j-1]
                p[i][j] = 1
            elif j == 0:
                a[i][j] += a[i-1][j]
                p[i][j] = 2
            else:
                if a[i-1][j] >= a[i][j-1]:
                    p[i][j] = 2
                else:
                    p[i][j] = 1
                a[i][j] += max(a[i-1][j], a[i][j-1])
    path(p, n-1, m-1, [])
    return a[n-1][m-1]

a = [[5,3,2,2],
    [2,1,7,3],
    [4,3,1,2]]

a2 = [[1,4,1,2,3],
    [2,3,2,1,4],
    [1,1,1,2,4],
    [2,5,1,7,1]]

print(bug(a))
