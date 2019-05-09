def solution(n):
    cnt = 0
    while n != 0:
        if n % 2:
            cnt += 1
        n = n // 2
    return cnt