n = 3
a = [''] * (n*2)

def check_line(line):
    s = []
    for i in range(len(line)):
        c = line[i]
        if c == '(' or c == '[':
            s.append(c)
        else:
            if len(s) == 0:
                return False
            t = s.pop()
            if t == '(' and c == ')':
                continue
            if t == '[' and c == ']':
                continue
            return False
    return len(s) == 0

iter = 1
out = 20

def rec(stack):
    global iter
    if len(stack) == 2 * n:
        if check_line(''.join(stack)):
            if iter == out:
                print(''.join(stack))
                exit(1)
            elif out == -1:
                print(''.join(stack))
            iter += 1
        return
    if len(stack) == 0:
        stack.append('(')
        rec(stack)
        stack.pop()
        stack.append('[')
        rec(stack)
        stack.pop()
        return

    last = stack.pop()
    stack.append(last)
    if last == ')' or last == ']':
        for i in "()[]":
            stack.append(i)
            rec(stack)
            stack.pop()
    elif last == '(':
        for i in "()[":
            stack.append(i)
            rec(stack)
            stack.pop()
    elif last == '[':
        for i in "([]":
            stack.append(i)
            rec(stack)
            stack.pop()

rec([])
