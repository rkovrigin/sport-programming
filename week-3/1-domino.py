def domino(n, m = 2):
    out = [0] * n
    for i in range(m):
        out[i] = 1
    out[m-1] = 2
    for i in range(m, n):
        out[i] = out[i-1] + out[i-m]
    print(out)
    return out[-1]

print(domino(10, 2))
print(domino(10, 3))
