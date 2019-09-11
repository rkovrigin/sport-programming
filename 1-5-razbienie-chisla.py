n = 35
a = [0] * n
index = 1
out_index = 13672

def rec(idx, sum, last):
    global index
    if sum == n:
        if index == out_index:
            print([i for i in a if i > 0])
        index += 1
    for i in range(last, n - sum + 1):
        a[idx] = i
        rec(idx + 1, sum + i, i)
        a[idx] = 0

rec(0, 0, 1)
