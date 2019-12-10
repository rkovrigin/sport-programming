shop = [135, -478, -181, 39, 55, 166, 85, 274, -220, 455]
warehouse = [-488, 389, 138, 392, -398, -38, 16, 72, -456, -196]

# shop = [3, 5]
# warehouse = [6, 2]

with open('shops2.in', 'r') as f:
    _ = f.readline()
    shop = [int(i) for i in f.readline().split()]
    warehouse = [int(i) for i in f.readline().split()]

shop.sort(reverse=True)
warehouse.sort(reverse=True)

print(sum([abs(i - j) for i,j in zip(shop, warehouse)]))
exit()
out = []
for s in shop:
    tmp = abs(s - warehouse[0])
    _w = warehouse[0]
    for w in warehouse:
        if abs(s - w) < tmp:
            tmp = abs(s - w)
            _w = w
    print("%d %d" % (s, _w))
    out.append(abs(s - _w))
    warehouse.remove(_w)
print(out, sum(out))
