# My solution

def solution(n, m):
    a = max(n, m)
    b = min(n, m)
    num = a % b
    while num > 0:
        a = b
        b = num
        num = a % b
    return [b, (n * m) // b]