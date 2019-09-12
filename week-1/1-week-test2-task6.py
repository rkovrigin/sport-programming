s = [
"()()[[[]()]]([()][][()[]])[]()()",
"[[]](()()[[[]]][]()()()[()])()]",
"[]()[](((()]))(()()[][])[]([])[]",
"[[]][()[)[]([][]]()][]()()(())()",
"(()[([][]())[()][()][][]])([])()",
"[(])",
"[][()]",
"[)(]",
"([())]"]

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
    return True



line = "[(])"
res = check_line(line)
print(line, res)

for line in s:
    res = check_line(line)
    print(line, res)
