import sys
sys.stdin = open("종이붙이기_input.txt")

# 일반 코드

# def combination(N, M):
#     if M == 0 or (N == M):
#         return 1

#     zero, pole = 1, 1

#     for i in range(N-M+1, N+1):
#         zero *= i
#         pole *= ((N+1)-i)

#     return zero // pole

# T = int(input())

# for n in range(1, T+1):
#     N = int(input()) // 10
#     square = 0
#     result = 0
#     while N >= 0: 
#         result += combination(N+square, square) * 2**square
#         N += -2
#         square += 1
#     print(f"#{n} {result}")

#####################################################################################
# 재귀함수 사용

T = int(input())

def paper(n):
    if n == 0:
        return 1
    elif n - 2 < 0:
        return paper(n-1) 
    return paper(n-1) + paper(n-2)*2

for n in range(1, T+1):
    N = int(input()) // 10
    print(f"#{n} {paper(N)}")