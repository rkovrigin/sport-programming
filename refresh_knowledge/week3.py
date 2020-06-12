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

change(23, [1,3, 7])
