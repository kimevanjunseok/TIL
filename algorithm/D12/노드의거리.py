import sys
sys.stdin = open('노드의거리_input.txt')

T = int(input())

def gogo(L, x):

    global visited, route_2, result

    visited.append(x)

    if len(visited) -1 > result:
        visited.pop()
        return

    if visited[-1] == start_end[1]:
        result = len(visited)-1
        visited.pop()
        return

    for i in range(1, V+1):
        if (L[i] == 1) and (i not in visited):  
            gogo(route_2[i], i)
    
    visited.pop()

for n in range(1, T+1):
    V, E = map(int, input().split())
    route = [list(map(int, input().split())) for i in range(E)]
    route_2 = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in route:
        route_2[i[0]][i[1]] = 1
        route_2[i[1]][i[0]] = 1
    start_end = list(map(int, input().split()))
    visited = []
    result = E+1

    gogo(route_2[start_end[0]], start_end[0])

    print(f'#{n} {0 if result == E+1 else result}')