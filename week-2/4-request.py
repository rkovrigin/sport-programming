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
applications = zip(left, right)
applications.sort(key=lambda x: x[1])
application_choice(applications)
