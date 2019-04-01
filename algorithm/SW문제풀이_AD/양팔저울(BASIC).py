def powerset(x, y):
    if x == y:
        L = []
        for i in range(y):
            if t[i]:
                L.append(chu[i])
        if sum(L) not in sum_chu:
            sum_chu.append(sum(L))
        return

    else:
        powerset(x+1, y)
        t[x] = True
        powerset(x+1, y)
        t[x] = False

def sol(z):
    global N, judge
    for i in range(len(sum_chu)):
        if sum_chu[i] + z in sum_chu:
            judge = 1
            return

N = int(input())
chu = list(map(int, input().split()))
M = int(input())
Gi = list(map(int, input().split()))
sum_chu = []
t = [False] * N
powerset(0, N)
sum_chu.pop(0)
tx = [False] * len(sum_chu)
for i in range(len(Gi)):
    judge = 0
    if Gi[i] in sum_chu:
        print("Y", end=" ")
    else:
        sol(Gi[i])
        if judge:
            print("Y", end=" ")
        else:
            print("N", end=" ")

