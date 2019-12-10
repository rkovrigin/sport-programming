shop = [135, -478, -181, 39, 55, 166, 85, 274, -220, 455]
warehouse = [-488, 389, 138, 392, -398, -38, 16, 72, -456, -196]

# shop = [3, 5]
# warehouse = [6, 2]

out = []
for s in shop:
    tmp = 10000000
    _w = 10000000
    for w in warehouse:
        if abs(s - w) < tmp:
            tmp = abs(s - w)
            _w = w
    print("%d %d" % (s, _w))
    out.append(abs(s - _w))
    warehouse.remove(_w)
print(out, sum(out))
