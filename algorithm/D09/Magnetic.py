import sys
sys.stdin = open('Magnetic_input.txt')

T = 10

for n in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        change = 0
        for j in range(N):
            if arr[j][i] == 1:
                change = 1
            elif arr[j][i] == 2:
                if change == 1:
                    result += 1
                    change = 0

    print(f'#{n} {result}')
