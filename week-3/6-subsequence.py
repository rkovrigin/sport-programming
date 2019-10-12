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
    # print(d)
    for i in d:
        print(i)
    print(d[n][m])

with open("seq2.in", 'r') as f:
    f.readline()
    a = [int(i) for i in f.readline().split()]
    f.readline()
    b = [int(i) for i in f.readline().split()]
    subsequence(a, b)
