def mask_perebor(n):
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                print i+1,
        print ''

def mask_perebor_lexograph(n):
    for mask in range(1 << n)[::-1]:
        for i in range(n, -1, -1):
            if mask & (1 << i):
                print n-i,
        print ''

mask_perebor(3)
print "---"
mask_perebor_lexograph(3)
