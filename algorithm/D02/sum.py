import sys
sys.stdin = open("sum_input.txt")

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    min_num_list = num_list[0:M]
    max_num_list = num_list[0:M]
    min_num = 0
    max_num = 0
    sample_num = 0

    for i in range(M):
            min_num += min_num_list[i]
            max_num += max_num_list[i]

    for i in range(1, N - M + 1):
        sample_list = num_list[i:M+i]
        for j in range(M):
            sample_num += sample_list[j]
        if min_num > sample_num:
            min_num = sample_num
        elif max_num < sample_num:
            max_num = sample_num

        sample_list = []
        sample_num = 0

    result = max_num - min_num

    print(f'#{n} {result}')