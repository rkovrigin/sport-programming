def domino(n, m, mod):
    out = [0] * n
    for i in range(m):
        out[i] = 1
    out[m-1] = m
    # print(out)
    for i in range(m, n):
        out[i] = out[i-1] + out[i-m]
        out[i] %= mod
    # print(out)
    return out[-1]


out = domino(100000, 2, 1000000000)
print(out)
