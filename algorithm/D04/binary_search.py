import sys
sys.stdin = open("binary_search_input.txt")

T = int(input())

for i in range(1, T+1):
    P, A, B = map(int, input().split())
    start_A, end_A = 1, P
    start_B, end_B = 1, P
    cnt_A, cnt_B = 0, 0

    while True:
        middle_A = (start_A + end_A) // 2
        middle_B = (start_B + end_B) // 2
        if A == middle_A and B == middle_B:
            result = 0
            break

        if A == middle_A:
            result = "A"
            break
        elif A < middle_A:
            end_A = middle_A
        else:
            start_A = middle_A

        if B == middle_B:
            result = "B"
            break
        elif B < middle_B:
            end_B = middle_B
        else:
            start_B = middle_B

        cnt_A += 1
        cnt_B += 1

    print(f"#{i} {result}")

