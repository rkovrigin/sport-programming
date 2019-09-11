n = 10
m = 3
p = [''] * n

def rec(idx, m, last):
    if m < 0:
        return
    if m == 0 and idx == n:
        print(p)
    for i in range(idx, n):
        if last == '*':
            p[i] = '.'
            rec(i + 1, m, '.')
        else:
            p[i] = '*'
            rec(i + 1, m - 1, '*')
            p[i] = '.'
rec(0, m, '')
