n = 4
m = 2

a = [0] * n
index = 1
out_index = 3

def rec(idx):
    global index
    if idx == n:
        if index == out_index:
            print (a, index)
        index += 1
        print(a)
        return
    for i in range(1, m + 1):
        a[idx] = i
        rec(idx + 1)
rec(0)
