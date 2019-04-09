def solution(n):
    cnt = 0
    for i in range(1, n+1):
        sums = 0
        for j in range(i, n+1):
            sums += j
            if sums >= n:
                if sums == n:
                    cnt += 1
                break
    return cnt