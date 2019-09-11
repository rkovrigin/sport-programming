n = 4
a = [[0,1,4,6],
     [1,0,5,2],
     [4,5,0,3],
     [6,2,3,0],]

used = [False] * (n)
p = [0] * (n)
ans = 10000

def rec(idx, len):
    global ans
    if len >= ans:
        return
    if idx == n:
        ans = min(ans, len + a[p[idx-1]][0])
        return
    for i in range(1, n):
        if used[i]:
            continue
        p[idx] = i
        used[i] = True
        rec(idx + 1, len + a[p[idx-1]][i])
        used[i] = False

p[0] = 0
rec(1, 0)
print(ans)
