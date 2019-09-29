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
