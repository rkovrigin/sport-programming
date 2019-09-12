n = 6
m = 4
out_index = -1
a = [0] * n
index = 1


def rec(idx):
    global index
    if idx == n:
        if out_index == -1 or index == out_index:
            print (a, index)
        index += 1
        # print(a)
        return
    for i in range(1, m + 1):
        a[idx] = i
        rec(idx + 1)
rec(0)
