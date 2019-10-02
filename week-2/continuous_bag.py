n, W = 0, 0
w, c = None, None

with open("count2.in") as f:
    n, W = [int(i) for i in f.readline().split()]
    w, c = [0] * n, [0] * n
    for i in range(n):
        w[i], c[i] = [int(v) for v in f.readline().split()]

    print(n, W)
    print(w, '\n', c)

# wc = zip(w, c)
# wc.sort(key=lambda x: x[1], reverse=0)
# print(wc)

# w = [2, 3]
# c = [10, 12]
# n, W = 2, 4

wc = zip(w, c)
wc.sort(key=lambda x: x[1]//x[0], reverse=0)
print(wc)

def fill_bag(n, W, wc):
    weight = 0
    price = 0
    while len(wc) > 0 and weight < W:
        tmp = wc.pop()
        if weight + tmp[0] <= W:
            weight += tmp[0]
            price += tmp[1]
            print("+W = ", tmp[0], tmp[1])
        else:
            ppk = tmp[1] // tmp[0]
            ost = W - weight
            price += ost * ppk
            weight = W
            print("+Wost = ", ost * ppk)
    print(weight, price)

fill_bag(n=n, W=W, wc=wc)
