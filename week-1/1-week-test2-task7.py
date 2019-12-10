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
out = -1

def rec_(stack):
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
# rec2([])


def rec(stack, out, idx):
    if idx == n * 2:
        print(out)
        return
    for c in "()[]":
        if len(stack) == 0:
            if c == '(' or c == '[':
                stack.append(c)
            elif c == ')' or c == ']':
                break
        elif out[idx] == '[' and c == ')':
            break
        elif out[idx] == '(' and c == ']':
            break
        elif stack[-1] == '(' and c == ')':
            out[idx] = ')'
            out[len(stack)] = '('
            stack.pop()
        elif stack[-1] == '[' and c == ']':
            out[idx] = ']'
            out[idx-1]   d = '['
            stack.pop()
        rec(stack, out, idx + 1)

rec([], a, 0)
