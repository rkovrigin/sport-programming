def mask_perebor(n):
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                print i+1,
        print ''

def mask_perebor_lexograph(n, x=-1):
    tmp = 1
    out = []
    for mask in range(1 << n)[::-1]:
        out.append([])
        for i in range(n, -1, -1):
            if mask & (1 << i):
                out[-1].append(n-i)
                print n-i,
        print ''
    if x != -1:
        print(out[x-1])
    else:
        print(out)

# mask_perebor(3)
print "---"
mask_perebor_lexograph(9, 365)
