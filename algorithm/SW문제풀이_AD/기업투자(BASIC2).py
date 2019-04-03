def perm(x, y):
    global ea, maxN
    if x == y:
        sums = 0
        for i in range(ea):
            if t[i] != 0:
                sums += arr[t[i]-1][i+1]
        if maxN < sums:
            maxN = sums
    else:
        for i in range(x, y):
            t[i], t[x] = t[x], t[i]
            perm(x+1, y)
            t[i], t[x] = t[x], t[i]

def combi(x, y):
    global money, ea
    if y == 0:
        if sum(t) == money:
            perm(0, ea)
            # print(t)
    elif x == 0:
        return
    else:
        t[y-1] = a[x-1]
        combi(x, y-1)
        combi(x-1, y)

money, ea = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(money)]
a = list(range(money+1))
maxN = 0
t = [0] * ea
combi(money+1, ea)
print(maxN)