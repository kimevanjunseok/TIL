import sys
sys.stdin = open("최소신장트리_input.txt")

def union(x, y):
    p[y] = x

def findset(x):
    if x == p[x]: return x
    else: return findset(p[x]) 

def mst():
    global V

    cnt = 0
    i = 0
    sums = 0
    while cnt < V:
        p1 = findset(arr[i][0])
        p2 = findset(arr[i][1])
        if p1 != p2:
            sums += arr[i][2]
            cnt += 1
            union(p1, p2)
        i += 1
    return sums

T = int(input())

for n in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key=lambda x:x[2])
    p = list(range(V+1))
    print("#{} {}".format(n, mst()))

