n = 3
a = [0] * n
used = [False] * n

def rec(idx):
    if idx == n:
        print(a)
        return
    for i in range(n):
        if used[i] is True:
            continue
        a[idx] = i
        used[i] = True
        rec(idx + 1)
        used[i] = False

rec(0)
