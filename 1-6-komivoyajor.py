n = 4
a = [[0,1,4,6],
     [1,0,5,2],
     [4,5,0,3],
     [6,2,3,0],]

used = [False] * n
p = [0] * n
ans = 10000

def rec(idx, len):
    global ans
    if len >= ans:
        return
    if idx == n:
        ans = min(ans, len + a[p[idx - 1]][0])
    for i in range(n):
        if used[i]:
            continue
        p[idx] = i
        used[idx] = True
        rec(idx + 1, len + a[p[idx] - 1][i])
        used[idx] = False
used[0] = True
rec(1, 0)
print(ans)
