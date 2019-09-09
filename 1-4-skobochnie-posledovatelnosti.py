def correct(s):
    bal = 0
    for c in s:
        if c == '(':
            bal += 1
        elif c == ')':
            bal -= 1
        else:
            print('Bad symbol', c)
            return False

        if bal < 0:
            return False
    return bal == 0

print(correct('()'))
print(correct('(()'))
print(correct(')('))
print(correct(')()'))
print(correct('((()))(()())'))
