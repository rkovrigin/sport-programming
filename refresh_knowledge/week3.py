def domino_3(n):
    x = [0 for _ in range(n)]
    x[0] = 1
    x[1] = 1
    x[2] = 2
    for i in range(3, n):
        x[i] = x[i-1] + x[i-3]
    print(x, x[-1])

#domino_3(10)


# l starts with 1, not with 0
def sum_1d_array(arr, l, r):
    s = [0 for _ in range(len(arr) + 1)]
    s[1] = arr[0]
    for i in range(1, len(s)):
        s[i] = arr[i-1] + s[i-1]

    print(s, "[%d:%d]" % (l, r), s[r] - s[l-1])

#sum_1d_array([1,2,3,4,5], 5,5)


#Change sum in coins
def recout(p, s):
    while s > 0:
        print(p[s])
        s -= p[s]

def change(s, coins):
    x = [0 for _ in range(s + 1)]
    p = [0 for _ in range(s + 1)]

    for i in range(1, s+1):
        x[i] = s+1
        #without certificate
        #for coin in coins:
        #    if i - coin >= 0:
        #        x[i] = min(x[i], x[i-coin] + 1)
        for coin in coins:
            if i - coin >= 0 and (x[i - coin] + 1) < x[i]:
                x[i] = x[i - coin] + 1
                p[i] = coin
    recout(p, s)
    print(x, x[-1])

#change(23, [1,3, 7])

def rukzak(p, w, W):
    d = [[0 for _ in range(W+1)] for _ in range(len(w))]
    print(d)

    for i in range(0, len(w)):
        for j in range(W+1):
            d[i][j] = d[i-1][j]
            if j - w[i] >= 0:
                d[i][j] = max(d[i][j], d[i-1][j-w[i]] + p[i])
    for _d in d:
        print(_d)

#rukzak([2,4,6], [1,5,7], 10)

#subsequence
def recout_sub(d, s, a):
    i = len(d) - 1
    j = len(d[0]) - 1
    w = ''

    while i>0 and j>0:
        di, dj = s[i][j]
        if d[i + di][j + dj] != d[i][j]:
            w = a[i-1] + w
            #print(a[i-1])
        i += di
        j += dj
    print(w)

def subsequence(a, b):
    n = len(a)
    m = len(b)
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]
    s = [[(0,0) for _ in range(m+1)] for _ in range(n+1)]

    #for i in range(1, n+1):
    #    for j in range(1, m+1):
    #        d[i][j] = max(d[i-1][j], d[i][j-1])
    #        if a[i-1] == b[j-1]:
    #            d[i][j] = max(d[i][j], d[i-1][j-1] + 1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if d[i - 1][j] > d[i][j - 1]:
                s[i][j] = (-1, 0)
                d[i][j] = d[i-1][j]
            else:
                s[i][j] = (0, -1)
                d[i][j] = d[i][j-1]
            if a[i-1] == b[j-1]:
                if d[i][j] < d[i-1][j-1] + 1:
                    s[i][j] = (-1, -1)
                    d[i][j] = d[i-1][j-1] + 1

    for row in d:
        print(row)
    for row in s:
        print(row)
    print("Len of max subsequence = %d" % d[n][m])
    recout_sub(d, s, a)

a = "abcd"
b = "a b c d"
subsequence([i for i in a], [i for i in b])
