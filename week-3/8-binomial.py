n = 50
k = 20

out = 0

def binomial(n, k):
    global out
    if n < 0 or k < 0:
        return
    if n == 0 or n == k:
        out += 1
        return
    binomial(n - 1, k - 1)
    binomial(n - 1, k)

def matrix_binomial(n, k):
    m = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n+1):
        m[i][0] = 1
        # print(m[i])
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                m[i][j] = 1
                continue
            m[i][j] = m[i-1][j-1] + m[i-1][j]
    # for i in range(n+1):
    #     print(m[i])
    print(m[n][k])

# binomial(n, k)
# print(out)
matrix_binomial(n, k)
