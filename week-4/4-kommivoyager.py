n = 4
# a = []
a = [[0,1,4,6],
     [1,0,5,2],
     [4,5,0,3],
     [6,2,3,0]]

INF = 100000
d = [[INF] * n for _ in range(1 << n)]
d[0][0] = 0

for mask in range(1 << n):
    for i in range(n):
        if d[mask][i] == INF: continue
        for j in range(n):
            if not mask & (1 << j):
                d[mask ^ (1 << j)][j] = min(d[mask ^ (1 << j)][j], d[mask][i] + a[i][j])
print(d)
print(d[(1 << n)-1][0])
