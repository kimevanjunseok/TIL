# My solution

def solution(a, b):
    M = max(a, b)
    N = min(a, b)
    answer = 0
    for i in range(N, M+1):
        answer += i
    return answer

####################################

# Other

def solution(a, b):
    return sum(range(min(a, b), max(a, b)+1))