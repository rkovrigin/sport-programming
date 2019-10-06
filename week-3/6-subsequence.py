def subsequence(a, b):
    n = len(a)
    m = len(b)
    d = [[0] * (m + 1) for i in range(n + 1)]
    print(d)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = max(d[i-1][j], d[i][j-1])
            if a[i-1] == b[j-1]:
                d[i][j] = max(d[i][j], d[i-1][j-1] + 1)
    print(d)
    print(d[n][m])


subsequence([1,2,3,4,5], [1,3,5])