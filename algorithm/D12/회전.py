import sys
sys.stdin = open('회전_input.txt')

T = int(input())

for n in range(1, T+1):
    N, M = map(int, input().split())
    queue = input().split()
    print(f"#{n} {queue[M%N]}")