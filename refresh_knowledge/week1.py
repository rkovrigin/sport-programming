"""
n - length
m - 1..m variants for permutations
"""
#with [2,1] != [1,2]
def perestanovki(n, m):
    x = [0 for i in range(n)]

    def rec(idx):
        if idx == n:
            print(x)
            return
        for i in range(1, m):
            x[idx] = i
            rec(idx + 1)
    rec(0)

#print("perestanovki ->")
#perestanovki(2, 3)

#with [2,1] == [1,2]
def perestanovki_no_repetitions(n, m):
    x = [0 for i in range(n)]
    used = [False for i in range(m)]

    def rec(idx):
        if idx == n:
            print(x)
            return
        for i in range(1, m):
            if used[i]:
                continue
            x[idx] = i
            used[i] = True
            rec(idx + 1)
            used[i] = False
    rec(0)

#print("perestanovki_no_repetitions ->")
#perestanovki_no_repetitions(2, 3)

"""
skobki of length n*2
"""
def skobki(n):
    x = ['' for i in range(n*2)]

    def rec(idx, bal):
        if bal > (n*2 - idx):
            return
        if bal < 0:
            return
        if idx == n*2:
            if bal == 0:
                print(x, bal, idx)
            return
        x[idx] = '('
        rec(idx + 1, bal + 1)
        x[idx] = ')'
        rec(idx + 1, bal - 1)
    rec(0, 0)
#skobki(4)

"""
Razbienie chisla na slagaemie
"""
def razbienie(n):
    x = [0 for i in range(n+1)]

    def rec(idx, last):
        if sum(x) == n:
            print(' '.join([str(i) for i in x if i]))
        if idx == n:
            return
        for i in range(last, n-sum(x)+1):
            x[idx] = i
            #print('*',x)
            rec(idx + 1, i)
            x[idx] = 0
    rec(0, 1)

razbienie(6)
