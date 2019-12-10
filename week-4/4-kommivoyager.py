n = 4

# a = [[0,1,4,6],
#      [1,0,5,2],
#      [4,5,0,3],
#      [6,2,3,0]]

a = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,0],
    [0,1,0,0]
]

# with open('salesman.in', 'r') as f:
#     n = int(f.readline())
#     a = []
#     for i in range(n):
#         a.append([int(i) for i in f.readline().split()])
# print(n, a)

def path(x, y, n, w, p):
    if w == 0:
        return
    next = 1000
    next_i = -1
    for i in p[n]:
        if i == INF:
            continue
        print([x],[y])
        if a[p[x][y]][i] < next:
            next = a[p[x][y]][i]
            next_i = i
    path(x-1, next_i, n, w - next, p)

INF = 10000000
d = [[INF] * n for _ in range(1 << n)]
p = [[INF] * n for _ in range(1 << n)]
d[0][0] = 0

for mask in range(1 << n):
    for i in range(n):
        if d[mask][i] == INF:
            continue
        for j in range(n):
            if not mask & (1 << j):#city j is not included
                d[mask | (1 << j)][j] = min(d[mask ^ (1 << j)][j], d[mask][i] + a[i][j])

                # if d[mask | (1 << j)][j] < d[mask][i] + a[i][j]:
                #     p[mask | (1 << j)][j] = j
                #     print j,
                # else:
                #     p[mask ^ (1 << j)][j] = i
                #     print i,
print ''

# for i in [1, 0b11, 0b111, 0b1111]:
#     print p[i]

for i in range(len(d)):
    for j in range(len(d[0])):
        print "%10d" % d[i][j],
    print '\t\t',
    for j in range(len(d[0])):
        print "%10d" % p[i][j],
    print ''

# path(len(p)-1, 0, n, d[(1 << n)-1][0], p)

print(d[(1 << n)-1][0])
