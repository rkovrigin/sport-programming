def backpack(w, c, W):
    n = len(w) # amount of items
    d = [[0] * (W + 1) for i in range(n)]
    # d = [[0] * (W + 1) for i in range(n + 1)]

    for i in range(0, n):
        for j in range(1, W + 1):
            d[i][j] = d[i-1][j]
            if j - w[i] >= 0:
                d[i][j] = max(d[i][j], d[i-1][j-w[i]] + c[i])
    for i in d:
        print i
    return d[-1][-1]


max_price = backpack([1,3,4,5], [1,4,5,7], 7)
print(max_price)
