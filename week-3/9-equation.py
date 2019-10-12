numbers = [1,2,3]
sm = 0
with open("arythm2.in", 'r') as f:
    _, sm = [int(i) for i in f.readline().split()]
    numbers = [int(i) for i in f.readline().split()]
    print(sm, '==', numbers)

def f(out, i):
    if i >= len(numbers):
        # print("OUT", out, sum(out))
        if sum(out) == sm:
            for i in out:
                if i >= 0:
                    print '+%d' % i,
                else:
                    print '%d' % i,
            exit(1)
        return
    f(out + [numbers[i] * -1], i + 1)
    f(out + [numbers[i]], i + 1)

out = [numbers[0]]
f(out, 1)
