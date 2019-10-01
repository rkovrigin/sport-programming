"""
This is example of hunger algorythm to change money with given coins;
It doesn't work properly because on every step it tries to do it 'optimally'
"""
def change(s, coins):
    cnt = 0
    for coin in coins:
        cnt += s // coin
        s %= coin
    return cnt

def true_change(s, coins):
    out = [0] * s
    for coin in coins:
        out[coin - 1] = 1
    print out
    for i in range(s):
        if out[i] != 0:
            continue
        for c in coins:
            if i - c >= 0:
                out[i] = out[i - c - 1] + 1
    print out

true_change(27, [1,2,8,10])
