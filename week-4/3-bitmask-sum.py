#n * 2^n

a = [1,2,3,4,5,6,7,8,9]
n = len(a)
sum = [0] * n

for mask in range(1 << n):
    for i in n:
        if mask & (1 << i):
            sum[mask] += a[i]


#2^n
for mask in range(1 << n):
    for i in n:
        if mask & (1 << i):
            sum[mask] = sum[mask ^ (1 << i)] + a[i]
            break
