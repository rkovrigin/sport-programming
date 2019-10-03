icecream = []
with open('ice2.in') as f:
    n = int(f.readline())
    for _ in range(n):
        icecream.append(f.readline().strip())

# icecream = ['vanilla20',
# 'pistachio',
# 'strawberry',
# 'blackberry',
# 'vanilla20',
# 'pistachio',
# 'pistachio',
# 'vanilla20']

print(icecream)
n = 1
tmp_icecream = []
for ice in icecream:
    if ice in tmp_icecream:
        tmp_icecream = [ice]
        n += 1
    else:
        tmp_icecream.append(ice)
print(n)
