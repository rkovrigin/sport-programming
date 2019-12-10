n = 10
a = [0] * n
used = [False] * n

index = 1
out_index = -1

def rec(idx):
    global index
    if idx == n:
        if index == out_index or out_index == -1:
            print(a)
        index += 1
        return
    for i in range(n):
        if used[i] is True:
            continue
        a[idx] = i + 1
        used[i] = True
        rec(idx + 1)
        used[i] = False

rec(0)
