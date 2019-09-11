from datetime import datetime


n = 25
m = 8
out = 24008
p = [''] * (n+1)
cur_index = -1

def rec(idx, m, last):
    if m < 0:
        return
    if m == 0 and idx == n:
        return
        # print(p)
    for i in range(idx, n):
        if last == '*':
            p[i] = '.'
            rec(i + 1, m, '.')
        else:
            p[i] = '*'
            rec(i + 1, m - 1, '*')
            p[i] = '.'

def rec2(idx, m, out_index=-1):
    global cur_index
    if m < 0:
        return
    if idx == n + 1:
        if m == 0:
            pass
            # if out_index == -1:
            #     print(''.join(p[1:]))
            # elif cur_index == out_index:
            #     print(' '.join(p[1:]))
            #     print(''.join(p[1:]))
            # cur_index += 1
        return
    for i in '*.':
        p[idx] = i
        if p[idx - 1] == '*' and p[idx] == '*':
            continue
        if p[idx] == '*':
            rec2(idx + 1, m - 1, out_index)
        else:
            rec2(idx + 1, m, out_index)

before = datetime.now()
rec2(1, m, out)
after = datetime.now()
print(after - before)
