n = 5
a = [0] * n

def rec(idx, sum, last):
    if sum == n:
        print([i for i in a if i > 0])
    for i in range(last, n - sum + 1):
        a[idx] = i
        rec(idx + 1, sum + i, i)
        a[idx] = 0

rec(0, 0, 1)
