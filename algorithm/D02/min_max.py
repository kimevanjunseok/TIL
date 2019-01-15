import sys
sys.stdin = open("min_max_input.txt")

T = int(input())

for n in range(1, T+1):
    num = int(input())
    num_list = list(map(int, input().split()))

    for i in range(len(num_list)-1, 0, -1):
        for j in range(i):
            if num_list[j] < num_list[j+1]:
                num_list[j],  num_list[j+1] = num_list[j+1],  num_list[j]

    print(f'#{n} {num_list[0] - num_list[-1]}')