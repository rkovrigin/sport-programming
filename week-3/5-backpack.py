def recout(W, d, w, n):
    for i in range(len(w)-1, -1, -1):
        if d[i][W] != d[i-1][W]:
            W -= w[i]
            print(W, w[i], i)
        print("{%d}"% i)

def backpack(w, c, W):
    n = len(w) # amount of items
    d = [[0] * (W + 1) for i in range(n)]
    r = [[0] * (W + 1) for i in range(n)]

    for i in range(0, n):
        for j in range(1, W + 1):
            d[i][j] = d[i-1][j]
            if j - w[i] >= 0:
                d[i][j] = max(d[i][j], d[i-1][j-w[i]] + c[i])
                r[i][j] = i
    for i in d:
        print i
    print('')
    # for i in r:
    #     print i
    # print(r[-1][-1], d[-1][-1], w, c)
    recout(W, d, w, n)
    return d[-1][-1]

# with open("rucksack.in", 'r') as f:
#     n, W = [int(i) for i in f.readline().split()]
#     w, p = [0] * n, [0] * n
#     for i in range(n):
#         w[i], p[i] = [int(t) for t in f.readline().split()]
#     max_price = backpack(w, p, W)
#     print(max_price)

max_price = backpack([2,5,10], [10,20,30], 12)
print(max_price)
