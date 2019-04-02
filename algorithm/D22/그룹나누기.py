import sys
sys.stdin = open("그룹나누기_input.txt")

def union(x, y):
    p[findset(y)] = findset(x)

def findset(x):
    if x == p[x]: return x
    else: return findset(p[x])


T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = list(range(N+1))

    for i in range(0, len(arr), 2):
        union(arr[i], arr[i+1])

    for i in range(1, N+1):
        p[i] = findset(i)
    p.pop(0)
    print("#{0} {1}".format(n, len(set(p))))

    # ps = set()
    # for i in range(1, N+1):
    #     ps.add(findset(i))
    # print("#{0} {1}".format(n, len(ps)))


    # count = 0
    # for i in range(1, N+1):
    #     if i == p[i]: count += 1
    # print(count)




