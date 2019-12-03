def can(mask, new_mask):
    # l = max(len(bin(mask)), len(bin(new_mask))) - 2
    # _mask = [int(i) for i in format(mask, "0%db" % l)]
    # _new_mask = [int(i) for i in format(new_mask, "0%db" % l)]
    # tmp = 1
    # print (_mask)
    # print (_new_mask)

    # print (_new_mask)
    if mask & new_mask:
        return False
    full_mask = mask | new_mask
    fm = [int (i) for i in bin(full_mask)[2:]]
    tmp = 1

    for i in range(len(fm)):
        if tmp == 1:
            if fm[i] == 0:
                tmp = 0
            else:
                tmp = 1
        else:
            if fm[i]:
                return False
            else:
                tmp = 1
    if len(fm) > 1:
        if fm[-1] | fm[-2]:
            return False
    print(fm)
    return True

def can2(mask1, mask2, n=0):
    if mask1 & mask2:
        return False

    mask = mask1 | mask2
    # mask = 0b100011
    max = len(bin(mask)) - 2
    i = 0
    while i < max:
        m = ((3 << i) & mask) >> i
        print(f"{mask:0{max}b} {m:0{max}b} {m}")
        if m == 0 or m == 3:
            i += 2
        elif m == 1:
            i += 1
        elif m == 2:
            return False

    return True


def parket(n, m, mod = 10):
    d = [[0] * (1 << n) for i in range(m + 1)]
    # print (d)
    d[0][0] = 1
    for i in range(m):
        for mask in range(1 << n):
            for new_mask in range(1 << n):
                if can2(mask, new_mask):
                    d[i + 1][new_mask] += d[i][mask] % mod
                    # d[i + 1][new_mask] %= mod
    for i in d:
        print(d)
    print(d[m][0])

parket(2, 3, 10)
# parket(5, 6, 1000000000)
# print(can2(0b010001, 0b100010))
print(can2(0b0001, 0b1010))
