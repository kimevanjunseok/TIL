import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    for i in range(2, len(data)-1):
        if data[i-1] < data[i] and data[i-2] < data[i] and data[i+1] < data[i] and data[i+2] < data[i] :
            ans += data[i] - max(data[i-2], data[i-1], data[i+1], data[i+2])
    print("#{} {}".format(tc+1, ans))