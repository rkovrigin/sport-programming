def mask_perebor(n):
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                print i+1,
        print ''

mask_perebor(3)
