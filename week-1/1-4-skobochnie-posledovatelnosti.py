def correct(s):
    bal = 0
    for c in s:
        if c == '(':
            bal += 1
        elif c == ')':
            bal -= 1

        if bal < 0:
            return False
    return bal == 0


n, out_index = 10, 8644
a = [''] * n * 2
index = 1

def rec(idx, bal):
    global index
    if idx == n * 2:
        if bal == 0:
            if index == out_index or out_index == -1:
                print(''.join(a)), correct(''.join(a))
            index += 1
        return

    a[idx] = '('
    if bal < n*2 - idx: # check can we go further in or not
        rec(idx + 1, bal + 1)
    if bal == 0:
        return
    a[idx] = ')'
    rec(idx + 1, bal - 1)

rec(0, 0)

# ss = ["((())())))",
# "(()))((())",
# "((((())))",
# "(()())(())",
# "(())(())()"]
# for s in ss:
#     print(s, correct(s))
