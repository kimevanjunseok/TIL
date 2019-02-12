import sys
sys.stdin = open("그래프경로_input.txt")

T = int(input())

for n in range(1, T+1):
    V, E = map(int, input().split())
    route = []
    for i in range(E):
        route.append(list(map(int, input().split())))
    come = [False] * E
    print(route)
    end = list(map(int, input().split()))
    road = [[end[0], end[0]]]
    result = 0
    while len(road) != 0:
        cnt = 0
        while cnt != len(route):
            if road[-1][1] == route[cnt][0] and come[cnt] == False:
                road += [route[cnt]]
                come[cnt] = True
                cnt = -1
                if road[-1][1] == end[1]:
                    result = 1
                    break
            cnt += 1
        road.pop()

    print(f"#{n} {result}")

#################################################################################

# 재귀함수 사용

T = int(input())

def gogo(v):
    global route, come, end
    value = v.pop()
    if value[1] == end[1]:
        L.append(end[1])
    
    for i in range(len(route)):
        if value[1] == route[i][0] and come[i] == False:
            come[i] = True
            gogo([route[i]])

for n in range(1, T+1):
    V, E = map(int, input().split())
    L = []
    route = [list(map(int, input().split())) for i in range(E)]
    come = [False] * E
    end = list(map(int, input().split()))
    gogo([[ end[0], end[0] ]])
    print(f"#{n} {1 if L else 0}")
