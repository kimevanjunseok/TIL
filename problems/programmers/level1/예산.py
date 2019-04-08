# My solution

def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if budget >= sum(d):
            answer = len(d)
        elif budget < sum(d[:i+1]):
            answer = i
            break
    return answer