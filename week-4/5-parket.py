def can(mask, new_mask):
    l = max(len(bin(mask)), len(bin(new_mask))) - 2
    _mask = [int(i) for i in format(mask, "0%db" % l)]
    _new_mask = [int(i) for i in format(new_mask, "0%db" % l)]
    tmp = 0
    if mask & new_mask:
        return False
    for i in range(len(_mask)):
        if tmp == 0:
            if _mask[i] | _new_mask[i] == 0:
                tmp = 1
            else:
                tmp = 0
        else:
            if _mask[i] | _new_mask[i]:
                return False
            else:
                tmp = 0
    return True

def parket(n, m, mod = 1):
    d = [[0] * (1 << n) for i in range(m + 1)]
    # print (d)
    d[0][0] = 1
    for i in range(m):
        for mask in range(1 << n):
            for new_mask in range(1 << n):
                if can(mask, new_mask):
                    d[i + 1][new_mask] += d[i][mask]
                    # d[i + 1][new_mask] %= mod
    for i in d:
        print(d)
    print(d[m][0])

parket(3, 2)
# print(can(0b010001, 0b100010))
