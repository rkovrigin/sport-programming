periods = []
with open('request2.in', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        periods.append([int(v) for v in f.readline().split()])
periods.sort(key=lambda x: x[0])

def choose_apps(periods):
    timeline = []
    for period in periods:
        timeline.append((period[0], 'begin'))
        timeline.append((period[1], 'end'))
    timeline.sort(key=lambda x: x[0])

    print(timeline)
    m = 0
    out = 0
    for t in timeline:
        if t[1] == 'begin':
            m += 1
        else:
            m -= 1
        out = max(out, m)
    print(out)

choose_apps([[1,5], [3,6], [5,7]])
choose_apps(periods)
