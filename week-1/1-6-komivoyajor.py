n = 10
a = []
a = [[0,1,4,6],
     [1,0,5,2],
     [4,5,0,3],
     [6,2,3,0],]
n = 4
# 0  41 67  0 78  5 91  4 18 67
# 41  0 34 69 58 45 95  2 95 99
# 67 34  0 24 62 81 42 53 47 35
#  0 69 24  0 64 27 27 92 26 94
# 78 58 62 64  0 61 36 82 71  3
# 5  45 81 27 61  0 91 21 38 11
# 91 95 42 27 36 91  0 16 69 22
#  4  2 53 92 82 21 16  0 12 33
# 18 95 47 26 71 38 69 12  0 73
# 67 99 35 94  3 11 22 33 73  0

used = [False] * (n)
p = [0] * (n)
out_p = None
ans = 10000000

def rec(idx, len):
    global ans
    global out_p
    if len > ans:
        return
    if idx == n:
        # ans = min(ans, len + a[p[idx-1]][0])
        if ans > len + a[p[idx-1]][0]:
            ans = len + a[p[idx-1]][0]
            print(p, ans)
            out_p = p[:]
        return
    for i in range(1, n):
        if used[i]:
            continue
        p[idx] = i
        used[i] = True
        rec(idx + 1, len + a[p[idx-1]][i])
        used[i] = False

def main():
    global a

    # with open("1-week-input-test2-task4", 'r') as f:
    #     o = f.read()
    #     o = o.split('\n')
    #     print(o)
    #     a = []
    #     for line in o[1:]:
    #         if len(line) > 0:
    #             a.append([int(i) for i in line.split(' ')])
    # print(a)

    p[0] = 0
    rec(1, 0)
    print(ans)
    print(out_p)

if __name__ == '__main__':
    main()
