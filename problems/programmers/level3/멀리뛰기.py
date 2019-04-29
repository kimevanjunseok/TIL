def solution(N):
    def conbi(n, r):
        x = y = z = 1
        for i in range(1, n+1):
            x *= i
        for i in range(1, r+1):
            y *= i
        for i in range(1, n-r+1):
            z *= i
        return x // (y*z)
    answer = 0
    cnt = 0
    if N % 2:
        while N >= cnt+1:
            answer += conbi(N, cnt)
            N += -1
            cnt += 1
    else:
        while N >= cnt:
            answer += conbi(N, cnt)
            N += -1
            cnt += 1

    return answer % 1234567