"""
n - orders
d[i] - deadline of i'th order
c[i] - price of i'th order
For every order it takes 1 day to fulfill an order.
1 <= n <= 5000
1 <= d <= 5000
1 <= c <= 10^9
Task - maximize amount of money.
"""

#not a canonical algorythm; In canonical they sort deadline in descending order
def schedule(deadline, price):
    out = [0] * len(deadline)
    for i in range(len(out)):
        p = price[i]
        d = deadline[i]
        for j in range(d - 1, -1, -1):
            if out[j] == 0:
                out[j] = p
                break
            else:
                out[j] = max(out[j], p)

    print(out, ' ', sum(out))

deadline = [1,2,2,3,5]
price    = [2,5,4,1,3]
deadline = [2,2,1,7,5,5,4,7,7,5]
price    = [92,80,66,55,55,38,35,19,16,2]

with open("schedule.txt", 'r') as f:
    n = int(f.readline())
    print(n)
    deadline = [0] * n
    price    = [0] * n
    for i in range(n):
        line = f.readline()
        if line:
            deadline[i], price[i] = [int(v) for v in line.split(' ')]
schedule(deadline=deadline, price=price)
