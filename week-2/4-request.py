"""
N applications [l, r)
Find as max of not intersect applications
"""
def application_choice(applications):
    cnt = 1
    last = 0
    print(applications)
    for i in range(1, len(applications)):
        if applications[i][0] >= applications[last][1]:
            cnt += 1
            last = i
    print(cnt)

left  = [1,2,4,7]
right = [3,4,6,8]

with open("request2.in", 'r') as f:
    n = int(f.readline())
    print(n)
    left = [0] * n
    right    = [0] * n
    for i in range(n):
        line = f.readline()
        if line:
            left[i], right[i] = [int(v) for v in line.split(' ')]


applications = zip(left, right)
applications.sort(key=lambda x: x[1])
application_choice(applications)
