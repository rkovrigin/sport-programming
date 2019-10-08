def longest_ascending_sequence(a):
    d = [0] * len(a)
    c = [0] * len(a)

    for i in range(0, len(d)):
        d[i] = 1
        for j in range(0, i):
            if a[j] <= a[i]:
                d[i] = max(d[i], d[j] + 1)
                c[d[i]] += 1
    mx = max(d)
    count = 0
    for i in range(len(d)):
        if d[i] == mx:
            count += 1
            print(d[i], i)
    print(count)
    print(c[mx-1], c[mx], c[mx+1])

with open('lis.in', 'r') as f:
    f.readline()
    a = [int(i) for i in f.readline().split()]
    longest_ascending_sequence(a)
