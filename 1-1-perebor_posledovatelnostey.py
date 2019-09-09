n = 2
m = 3

a = [0] * n

def rec(idx):
    if idx == n:
        print a
        return
    for i in range(m):
        a[idx] = i
        rec(idx + 1)
rec(0)
