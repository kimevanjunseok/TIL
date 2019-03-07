import sys
sys.stdin = open('보물상자비밀번호_input.txt')

T = int(input())

def trans(x):
    global result
    x = x[::-1]
    for i in range(len(x)):
        if x[i] in ['A', 'B', 'C', 'D', 'E', 'F']:
            if x[i] == 'A':
                result += 10 * (16**i)
            elif x[i] == 'B':
                result += 11 * (16**i)
            elif x[i] == 'C':
                result += 12 * (16**i)
            elif x[i] == 'D':
                result += 13 * (16**i)
            elif x[i] == 'E':
                result += 14 * (16**i)
            elif x[i] == 'F':
                result += 15 * (16**i)
        else:
            result += int(x[i]) * (16**i)



for n in range(1, T+1):
    N, K = map(int, input().split())
    arr = input()
    arr = arr + arr[:(N//4)-1]
    stack = []
    S = ''
    result = 0
    for i in range(N):
        if arr[i:i+(N//4)] not in stack:
            stack.append(arr[i:i+(N//4)])
    stack.sort(reverse=True)
    trans(stack[K-1])
    print("#{0} {1}".format(n, result))
