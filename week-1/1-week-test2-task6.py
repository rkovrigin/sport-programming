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
    a = 0
    b = 0
    for i in range(len(line)):
        c = line[i]
        if c == '(':
            a += 1
        elif c == ')':
            a -= 1
        elif c == '[':
            b += 1
        elif c == ']':
            b -= 1

        if i > 0:
            if line[i] == ')' and line[i - 1] == '[':
                return False
            if line[i] == ']' and line [i - 1] == '(':
                return False

        if a < 0 or b < 0:
            return False
    return a == 0 and b == 0

line = "[(])"
res = check_line(line)
print(line, res)

for line in s:
    res = check_line(line)
    print(line, res)
