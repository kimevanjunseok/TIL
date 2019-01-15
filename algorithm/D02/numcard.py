import sys
sys.stdin = open("numcard_input.txt")

N = int(input())

for T in range(1, N+1):
    num = int(input())
    nums = list(map(int, input()))
    cnt_list = [0] * 10

    for i in nums:
        cnt_list[i] += 1
    count_num = cnt_list[0]

    for i in range(1, len(cnt_list)):
        if count_num <= cnt_list[i]:
            result_num = i
            count_num = cnt_list[i]

    print(f'#{T} {result_num} {count_num}')