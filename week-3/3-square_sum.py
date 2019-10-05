a = [[1,2,3], [2,3,4], [4,5,6]]
s = []

def prepare():
    x = len(a)
    y = len(a[0])
    for _ in range(x + 1):
        s.append([0] * (y + 1))

    for i in range(1, x+1):
        for j in range(1, y+1):
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i-1][j-1]
    print(s)

def square_sum(x1, x2, y1, y2):
    res = s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1]
    # print(s[x2][y2])
    # print(s[x1-1][y2])
    # print(s[x2][y1-1])
    # print(s[x1-1][y1-1])
    print(res)
    return res

prepare()
square_sum(2,3,1,3)
