import sys
sys.stdin = open('피자굽기_input.txt')

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    pizza = []
    
    for i in range(M):
        pizza.append([i+1, Ci[i]])

    result = 0
    queue = []

    for i in range(N):
        queue.append(pizza[i])

    while True:
        for i in range(len(queue)):
            queue[i][1] = queue[i][1]//2
            if N < M and queue[i][1] == 0:
                queue[i] = pizza[N]
                N = N+1
            elif N == M:
                cnt = 0
                for i in queue:
                    if i[1] == 0:
                        cnt += 1
                
                if cnt == len(queue) - 1:
                    for i in queue:
                        if i[1] != 0:
                            result = i[0]
        if result:
            break
            
    print(f'#{n} {result}')