def func1(x, List):
    global N
    if x == N:
        L = [0] * N
        for i in range(N):
            L[i] = List[i]
        result.append(L)
    else:
        for i in range(1, 7):
            List[x] = i
            func1(x+1, List)

def func2(x, List):
    global N
    if x == N:
        L = [0] * N
        for i in range(N):
            L[i] = List[i]

        if sorted(L) not in result:
            result.append(L)
    else:
        for i in range(1, 7):
            List[x] = i
            func2(x+1, List)

def func3(x, List):
    global N
    if x == N:
        L = [0] * N
        for i in range(N):
            L[i] = List[i]

        if len(set(L)) == N:
            result.append(L)
    else:
        for i in range(1, 7):
            List[x] = i
            func3(x+1, List)

N, M = map(int, input().split())
List = [0] * N
result = []

if M == 1:
    func1(0, List)

elif M == 2:
    func2(0, List)

elif M == 3:
    func3(0, List)

for i in result:
    print(*i)