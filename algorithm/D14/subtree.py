import sys
sys.stdin = open("subtree_input.txt")

def finder(x):
    global arr, result

    for i in range(0, len(arr), 2):
        if arr[i] == x:
            result += 1
            finder(arr[i+1])

T = int(input())

for n in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 1
    finder(N)
    print(f"#{n} {result}")