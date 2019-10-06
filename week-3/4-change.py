def recout(i, p):
    if i == 0:
        return
    recout(i - p[i], p)
    if i - p[i] > 0:
        print " + ",
    print p[i],

def change(n, coins):
    d = [n+1] * (n+1)
    p = [0] * (n+1)
    d[0] = 0
    for i in range(1, n + 1):
        for c in coins:
            if i - c >= 0 and d[i - c] + 1 < d[i]:
                d[i] = d[i - c] + 1
                p[i] = c
    print(d[-1])
    # print(p)
    recout(n, p)

change(488, [18,17])
