def recout(W, d, w, n):
    if W < 0 or n < 0:
        return
    if d[n][W] == 0:
        return
    if d[n-1][W] == d[n][W]:
        recout(W, d, w, n-1)
    else:
        recout(W - w[n], d, w, n-1)
        print(n)

def backpack(w, c, W):
    n = len(w) # amount of items
    d = [[0] * (W+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(0, W + 1):
            d[i][j] = d[i-1][j]
            if j - w[i-1] >= 0:
                d[i][j] = max(d[i][j], d[i-1][j-w[i-1]] + c[i-1])
    # for i in d:
    #     print i
    recout(W, d, w, n-1)
    return d[-1][-1]

with open("rucksack.in", 'r') as f:
    n, W = [int(i) for i in f.readline().split()]
    w, p = [0] * n, [0] * n
    for i in range(n):
        w[i], p[i] = [int(t) for t in f.readline().split()]
    max_price = backpack(w, p, W)
    print(max_price)

# max_price = backpack([6,4,3,2,5], [5,3,1,3,6], 15)
# print(max_price)
