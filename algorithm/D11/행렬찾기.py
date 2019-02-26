import sys
sys.stdin = open('행렬찾기_input.txt')

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    y = 0
    while y != N:
        x = 0 
        stand = y
        while x != N:
            if arr[x][y] != 0:
                x_cnt = x
                y_cnt = y
                while arr[x_cnt][y] != 0:
                    y += 1
                while arr[x][y_cnt] != 0:
                    x += 1
                result.append([(x-x_cnt)*(y-y_cnt),(x-x_cnt),(y-y_cnt)])
                for i in range(x_cnt, x):
                    for j in range(y_cnt, y):
                        arr[i][j] = 0
                y = stand
            x += 1
        y += 1

    result.sort()
    result_sort = []
    for i in result:
        for j in range(1, 3):
            result_sort += [f'{i[j]}']

    result_sort = " ".join(result_sort)
    
    print(f'#{n} {len(result)} {result_sort}')
