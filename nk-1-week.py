import time
from datetime import datetime
requiredIdx = None

def rec(idx, n, m, res):
    global requiredIdx
    if m < 0: return
    if idx == n:
        if m == 0:
            pass
            requiredIdx -= 1
            if requiredIdx == 0:
                print ("".join(res))
        return

    for i in "*.":
        if i == "*" and res[idx-1] == "*":
            continue
        if i == "*": m -= 1
        res[idx] = i
        rec(idx+1, n, m, res)
        if i == "*":
            m += 1

def main():
    global requiredIdx
    # n, m, requiredIdx = 7, 3, 7
    n, m, requiredIdx = 25, 8, 24008

    res = ["."] * n
    idx = 0
    t1 = time.time()
    before = datetime.now()
    rec(idx, n, m, res)
    after = datetime.now()
    print(after - before)
    print(time.time() - t1)

if __name__ == "__main__":
    main()
