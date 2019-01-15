import sys
sys.stdin = open("bus_input.txt")

T = int(input())

for n in range(1, T + 1):
    K, N, M = map(int, input().split())
    route = list(map(int, input().split()))
    charge_route = [0] * (N + K)
    charge_route[N] = 1

    for i in route:
        charge_route[i] = 1
    count = 0
    point = K

    while True:
        if charge_route[point] != 1:
            point += -1
        elif charge_route[point] == 1:
            count += 1
            charge_route = charge_route[point:]
            point = K
            if len(charge_route) == K:
                count += -1
                break

        if point == 0:
            count = 0
            break
    print(f'#{n} {count}')