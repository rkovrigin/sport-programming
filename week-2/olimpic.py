limit = 0
tasks = None
with open('contest.in', 'r') as f:
    _, limit = [int(v) for v in f.readline().split()]
    tasks = [int(v) for v in f.readline().split()]
# print(limit, tasks)

# limit = 60
# tasks = [30, 40, 20]

tasks.sort()
solved = []
for task in tasks:
    if limit - task >= 0:
        limit -= task
        solved.append(task)
for i in range(1, len(solved)):
    solved[i] += solved[i-1]
print(len(solved), sum(solved))
